import logging
import time

logger = logging.getLogger(__name__)
logging.basicConfig(filename='request.log', level=logging.INFO)

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

# def request_logging_middleware(get_response):
#     def middleware(request):
#         # Log request details
#         logger.info(f"Request: {request.method} {request.path}")

#         # Measure response time
#         start_time = time.time()
#         response = get_response(request)
#         duration = time.time() - start_time

#         # Log response time
#         logger.info(f"Response time: {duration:.2f}s")

#         return response

#     return middleware
