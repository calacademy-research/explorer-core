# middleware.py
import logging
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import authenticate, login, logout
from django.db import connection
from django.urls import reverse


logger = logging.getLogger(__name__)

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # logger.info("middleware __init__")

    def __call__(self, request):
        # Code to execute before the view is called
        # logger.info("middleware called")
        response = self.get_response(request)

        # Code to execute after the view is called
        # logger.info("middleware after view")
        response = self.process_response(request, response)

        return response

    def process_request(self, request):
        # Log the request path and method
        logger.info(f"middleware.py: Request path: {request.path}, Method: {request.method}")

        # Connect to MySQL database and obtain a cursor
        with connection.cursor() as cursor:
            # Checking specific paths
            if request.path == '/admin':
                logger.info("middleware.py: Landed on /admin page")
                self.handle_admin(request, cursor)
            elif request.path == '/login':
                logger.info("middleware.py: Handling login attempt")
                self.handle_login(request, cursor)
            elif request.path == '/logout':
                logger.info("middleware.py: Handling logout attempt")
                self.handle_logout(request, cursor)

    def handle_admin(self, request, cursor):
        # Example: Log admin access
        logger.info("middleware.py: Accessing /admin")
        print("middleware.py: Accessing /admin")
        # Perform any admin-specific logic using the cursor if needed
        # cursor.execute("SELECT * FROM some_table WHERE condition=%s", [value])

    def handle_login(self, request, cursor):
        logger.info("middleware.py: Handling /admin/login")
        print("middleware.py: Handling /admin/login")
        # Example: Handle login logic
        # if request.method == 'POST':
        #     # Example: Validate login credentials using the cursor
        #     username = request.POST.get('username')
        #     password = request.POST.get('password')
        #     cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", [username, password])
        #     user = cursor.fetchone()
        #
        #     if user:
        #         print("Login successful")
        #         # Perform any additional login actions, like setting session data
        #     else:
        #         return JsonResponse({'error': 'Invalid credentials'}, status=401)
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # User is authenticated, log them in
                login(request, user)
                # Example of database interaction (optional)
                cursor.execute("INSERT INTO user_logins (user_id, login_time) VALUES (%s, NOW())", [user.id])
                logger.info("Login successful")
                return JsonResponse({'message': 'Login successful'}, status=200)
            else:
                # User authentication failed
                return JsonResponse({'error': 'Invalid credentials'}, status=401)
        else:
            # Handle non-POST requests
            return JsonResponse({'error': 'Invalid request method'}, status=405)

    def handle_logout(self, request, cursor):
        # Example: Handle logout logic
        logger.info("middleware.py: Accessing /api/logout")
        # Perform any logout-specific logic using the cursor if needed
        # For example, clear session data
        if request.method == 'POST':
            if request.user.is_authenticated:
                # Log the user out
                logout(request)
                # Example: Log the logout action to the database (optional)
                cursor.execute("INSERT INTO user_logouts (user_id, logout_time) VALUES (%s, NOW())", [request.user.id])
                logger.info("Logout successful, session cleared")
                return JsonResponse({'message': 'Logout successful'}, status=200)
            else:
                # User is not logged in
                return JsonResponse({'error': 'User not logged in'}, status=400)
        else:
            # Handle non-POST requests
            return JsonResponse({'error': 'Invalid request method'}, status=405)

    #@staticmethod
    def process_response(self, request, response):
        # Any additional logic to be applied to the response

        logger.info("middleware.py: Processing response")
        response['X-Custom-Header'] = 'CalAcademy Collections API'

        # Example: Log the response status code
        logger.info(f"Response status code: {response.status_code}")

        # Optionally handle specific path-based responses
        if request.path == '/login' and response.status_code == 200:
            response['X-Login-Success'] = 'True'
        if request.path == '/api/recordset/' and response.status_code == 200:# and response.status_code == 200:
            response['X-Custom-Header'] = 'API Recordsets'
            # logger.info("landed on recordset page successfully")
        if request.path == '/api/occurrences/' and response.status_code == 200:
            response['X-Custom-Header'] = 'API Occurrences'
        if request.path == '/admin' and response.status_code == 200:
            response['X-Custom-Header'] = 'Django Admin Panel'
        return response

    def process_exception(self, request, exception):
        # Handle exceptions globally
        logger.error(f"middleware.py: Exception occurred: {exception}")
        logger.error(request)
        return JsonResponse({'error': 'Internal server error'}, status=500)

