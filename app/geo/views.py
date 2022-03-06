from django.conf import settings
from django.forms import URLField, ValidationError
from django.http import HttpResponse, JsonResponse
from geo.models import GeoLocation
from geo.serializers import GeoLocationSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import socket


def index(request):
    r = requests.get('http://api.ipstack.com/134.201.250.155?access_key=fede3473f1de34f0f209611a2c8aa9cf')
    print(r.json())
    return HttpResponse(r)

def validate_url(url):
    url_form_field = URLField()
    try:
        url = url_form_field.clean(url)
    except ValidationError:
        return False
    return True

def check_if_geo_loc_exist(id):
    try:
        geo_loc = GeoLocation.objects.get(id=id) 
    except GeoLocation.DoesNotExist:
        return False
    return geo_loc

def validate_ip(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return False
    return True

class GeoLocationListView(APIView):
    queryset = GeoLocation.objects.all()
    serializer_class = GeoLocationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        locations = GeoLocation.objects.all()
        serializer = GeoLocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        geo_loc_serializer = GeoLocationSerializer(data=request.data)
        if geo_loc_serializer.is_valid():
            geo_loc_serializer.save()
            return Response({}, status=status.HTTP_201_CREATED)
        return Response(geo_loc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_geo_loc(r):
    data = r.json()
    result = {
        'latitude': data['latitude'],
        'longitude': data['longitude']
    }
    return {'geo_location': result}

class GeoLocationView(APIView):

    queryset = GeoLocation.objects.all()
    serializer_class = GeoLocationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, ip_url):
        if not validate_url(ip_url) and not validate_ip(ip_url):
            return Response({'error': ip_url + " is not correct url or ip"})
        url = "http://api.ipstack.com/" + ip_url + "?access_key=" + settings.IPSTACK_KEY
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException as e:
            return Response({"Problem with connection, please try again later"})  
        formatted_res = get_geo_loc(r)           
        return JsonResponse(formatted_res)       

    def delete(self, request, ip_url):
        geo_loc = check_if_geo_loc_exist(int(ip_url))
        if geo_loc:
            geo_loc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
