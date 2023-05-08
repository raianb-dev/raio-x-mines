
from django.urls import resolve
from django.shortcuts import redirect
from django.urls import reverse

class NotFoundMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 404:
            try:
                resolve(request.path_info)
            except:
                return redirect(reverse('404'))

        return response
