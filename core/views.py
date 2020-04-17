from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from core.serializers import URLSerializer

from core.models import URL


class URLList(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = URL.objects.all()
    serializer_class = URLSerializer


@require_http_methods(['GET'])
def redirect_view(request, slug):
    try:
        obj = URL.objects.get(slug=slug)
        obj.access_counter += 1
        obj.save()
        return HttpResponseRedirect(f'{obj.full_url}')
    except Exception as e:
        return HttpResponseRedirect('/')