from .models import member, activities
from rest_framework import serializers


class memberserializers(serializers.ModelSerializer):
    class Meta:
        model = member
        fields = ('name', 'tz')


class activitiesserializers(serializers.ModelSerializer):
    class Meta:
        model = activities
        fields = ('user_id', 'start_time', 'end_time')
