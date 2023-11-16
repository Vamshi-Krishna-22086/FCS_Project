# middleware.py
import psutil
from django.http import HttpResponseServerError

class ResourceLimitMiddleware:
    def __init__(self, get_response, cpu_limit=80):
        self.get_response = get_response
        self.cpu_limit = cpu_limit

    def __call__(self, request):
        # Check CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        if cpu_percent > self.cpu_limit:
            return HttpResponseServerError("Server overloaded. Please try again later.")
        
        response = self.get_response(request)
        return response
