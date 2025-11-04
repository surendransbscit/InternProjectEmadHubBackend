from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
import time

class CustomMiddleware(MiddlewareMixin):
    time_out = 60

    def process_request(self, request):
        print(request)
        print("custommiddleware activated")
        request.start_time = time.time()
        # print(request.start_time)
        request.time_out = self.time_out
        print(self.time_out)

    def process_response(self, request, response):
        if hasattr(request, 'start_time'):
            # print("time", request.start_time)
            duration = time.time() - request.start_time
            print(f"request took {duration} seconds")
            if duration > request.time_out:
                return JsonResponse({'error': 'request timed out'}, status=408)
        return response
