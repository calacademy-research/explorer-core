from django.db import connections
import logging

logger = logging.getLogger(__name__)

class LogEndpointMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Log the status code and endpoint
        logger.info(f"Response status code: {response.status_code} for endpoint: {request.path}")
        return response


class CheckDBMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if info exists in the first database

        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT * FROM collectionsdb.collections_app_api_occurrence;")
            result = cursor.fetchone()
            # print("collectionsdb.collections_api_occurrence results: ", result)
        # with connections['default'].cursor() as cursor:
        #     cursor.execute("SELECT * FROM botanydb.collectingtrip;")
        #     result = cursor.fetchone()
        #     # print("botanydb.collectingtrip results: ", result)
        #
        #     # cursor.execute("SELECT * FROM botanydb.collectingtrip;")
        #     # result = cursor.fetchone()
        #     # print("botanydb.collectingtrip results: ", result)
        #     cursor.execute("SELECT * FROM botanydb.collectionobject;")
        #     result = cursor.fetchone()
        #     # print("botanydb.collectionobject results: ", result)
        #
            if result is None:
             exit("Database connection error in middleware_test.py")
        #     # Fetch info from the second database
        #     with connections['clusterdb'].cursor() as cursor:
        #         cursor.execute("SHOW TABLES;")
        #         #cursor.execute("SELECT * FROM clusterdb WHERE condition;")
        #         result = cursor.fetchone()
        #         #print("clusterdb table results: ", result)
        #
        #         if (result==None) or ("collectingtrip" not in result):
        #
        #         #     print("Creating collectingtrip table in clusterdb")
        #         #     cursor.execute("CREATE TABLE collectingtrip( CollectingTripID int, CollectingEventID int, TimestampCreated datetime, TimestampModified datetime, Collectingtripname varchar(400), EndDate date, EndDateVerbatim varchar(50), EndTime smallint, Remarks text, Sponsor varchar(64), StartDate date, StartDateVerbatim varchar(50), StartTime smallint, DisciplineID int, CreatedByAgentID int, ModifiedByAgentID int, EndDatePrecision tinyint, StartDatePrecision tinyint, Cruise varchar(250), Expedition varchar(250), Vessel varchar(250), CollectingTripAttributeID int, Agent1ID int, Agent2ID int);")
        #         #     #newresult = cursor.fetchone()
        #         #     # print("new clusterdb result: ", newresult)
        #         #     # request.cluster_info = newresult
        #         #     # newresponse = self.get_response(request)
        #         #     # return newresponse
        #         # else:
        #         #     print("Table collectingtrip already exists in clusterdb. Returning content of collectingtrip.clusterdb....")
        #         # cursor.execute("SELECT * FROM clusterdb.collectingtrip;")
        #         # result = cursor.fetchone()
        #
        #             with connections['casbotany'].cursor() as cursor:
        #                 cursor.execute("SHOW TABLES;")
        #                 result = cursor.fetchone()
        #                 print("Successfully connected to casbotany db, results: ", result)

        # Store the result in request for use in views
        request.cluster_info = result

        response = self.get_response(request)
        return response