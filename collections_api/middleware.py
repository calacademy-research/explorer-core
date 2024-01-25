import hmac
import time
from django.db import connections
from django.conf import settings
from rest_framework.response import Response
from django.utils.decorators import wraps




def get_record_sql_parser(table, columns, condition=None, limit=None):
    """used to parse sql SELECT statements for any table with optional
      filter conditions
      args:
        table: the tablename you desire to get data from
        columns: a list of column names to select if not, will default to "*"
        condition: optional condition(s) to filter data by.
    """
    sql = "SELECT "
    if columns:
        sql += ", ".join(columns)
    else:
        sql += "*" + " "

    sql += " " + f"FROM {table}"

    if condition:
        sql += " " + condition
    if limit:
        sql += " " + f"LIMIT {limit}"

    sql += ";"

    return sql


def generate_token(timestamp, filename):
    """Generate the auth token for the given filename and timestamp.
    This is for comparing to the client submited token.
    """
    timestamp = str(timestamp)
    if timestamp is None:
        print(f"Missing timestamp; token generation failure.")
    if filename is None:
        print(f"Missing filename, token generation failure.")
    mac = hmac.new(settings.KEY.encode(), timestamp.encode() + filename.encode(), digestmod='md5')
    return ':'.join((mac.hexdigest(), timestamp))


class TokenException(Exception):
    """Raised when an auth token is invalid for some reason."""
    pass


def get_timestamp():
    """Return an integer timestamp with one second resolution for
    the current moment.
    """
    return int(time.time())


def validate_token(token_in, filename):
    """Validate the input token for given filename using the secret key
    in settings. Checks that the token is within the time tolerance and
    is valid.
    """
    if settings.KEY is None:
        return
    if token_in == '':
        raise TokenException("Auth token is missing.")
    if ':' not in token_in:
        raise TokenException("Auth token is malformed.")

    mac_in, timestr = token_in.split(':')
    try:
        timestamp = int(timestr)
    except ValueError:
        raise TokenException("Auth token is malformed.")

    if settings.TIME_TOLERANCE is not None:
        current_time = get_timestamp()
        if not abs(current_time - timestamp) < settings.TIME_TOLERANCE:
            raise TokenException("Auth token timestamp out of range: %s vs %s" % (timestamp, current_time))

    if token_in != generate_token(timestamp, filename):
        raise TokenException("Auth token is invalid.")
    print(f"Valid token: {token_in} time: {timestr}")


def include_timestamp(func):
    """Decorate a view function to include the X-Timestamp header to help clients
    maintain time synchronization.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, Response):
            result['X-Timestamp'] = str(get_timestamp())
        return result

    return wrapper

def require_token(filename_param, always=False):
    """Decorate a view function to require an auth token to be present for access.

    filename_param defines the field in the request that contains the filename
    against which the token should validate.

    If REQUIRE_KEY_FOR_GET is False, validation will be skipped for GET and HEAD
    requests.

    Automatically adds the X-Timestamp header to responses to help clients stay
    synchronized.
    """

    def decorator(func):
        @include_timestamp
        @wraps(func)
        def wrapper(*args, **kwargs):
            request = args[0]  # Assuming request is the first argument
            if always or request.method not in ('GET', 'HEAD') or settings.REQUIRE_KEY_FOR_GET:
                params = request.data if request.method == 'POST' else request.query_params
                try:
                    validate_token(params.get('token'), params.get(filename_param))
                except TokenException as e:
                    return Response({'detail': f"403 - Forbidden. Invalid token: '{params.get('token')}'"}, status=403)
            return func(*args, **kwargs)

        return wrapper

    return decorator
