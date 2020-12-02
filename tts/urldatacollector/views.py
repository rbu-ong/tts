from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import loader

from urldatacollector.serializers import UrlSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import validators

from .models import url_data

def index(request):
    datas = url_data.objects.values()
    template = loader.get_template('base.html')
    context = {
        'datas': datas,
    }
    serializer = UrlSerializer(datas, many=True)
    return HttpResponse(template.render(context, request))

class RecordList(APIView):
    def get(self, request, format=None):
        data = url_data.objects.all()
        serializer = UrlSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        myDate = datetime.now()

        # Validate url.
        valid = validators.url(request.data['wloc'])
        if valid != True:
            return Response({"Fail": "Url is invalid"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if link already exist on the database.
        data = url_data.objects.filter(url=request.data['wloc']).values_list('id','url','count','date_added', 'date_updated').first()
        
        if data != None:
            # for response purposes
            temp_data = {
                'id': data[0],
                'url': data[1],
                'count': data[2] + 1,
                'date_added': data[3],
                'date_updated': data[4]
            }
            serializer = UrlSerializer(data=temp_data)
            if serializer.is_valid():
                # update the existing count and date_updated
                url_data.objects.filter(url = data[1]).update(count = data[2] + 1, date_updated = myDate.strftime("%Y-%m-%d %H:%M:%S"))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                'url': request.data['wloc'],
                'date_updated': myDate.strftime("%Y-%m-%d %H:%M:%S")
            }
            serializer = UrlSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)