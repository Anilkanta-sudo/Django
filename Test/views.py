from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import memberserializers, activitiesserializers
from .models import member
from .models import activities
import json
from datetime import datetime

f = member.objects.filter().values_list('id', flat=True)


# Create your views here.
@api_view(["POST"])
def add_meb_time(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        m = [i for i in f]
        if int(body['user_id']) not in m:
            tbl = member()
            tbl.name = body['name']
            tbl.tz = body['tz']
            tbl.save()
        tbl1 = activities()
        tbl1.user_id_id = body['user_id']
        tbl1.end_time = body['end_time']
        tbl1.start_time = body['start_time']
        tbl1.save()
        return Response(status.HTTP_201_CREATED)
    return Response(status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def show_list(request):
    if request.method == "GET":
        data = activities.objects.all()
        date_field = activitiesserializers(data, many=True)
        dataa = member.objects.all()
        meb_field = memberserializers(dataa, many=True)
        a = json.loads(json.dumps(meb_field.data))
        b = json.loads(json.dumps(date_field.data))
        f = member.objects.filter().values_list('id', flat=True)
        members = []
        details = []
        m = [i for i in f]
        for i in m:
            dat = member.objects.get(id=i)
            members.append({"id": i, "rel_name": dat.name, "tz": dat.tz})
            for j in b:
                if j['user_id'] == i:
                    details.append({"start_time": j['start_time'], "end_time": j['end_time']})
            if len(details) >= 1:
                members.append({"activity_details": details})
            details = []
        return Response({"members": members})
