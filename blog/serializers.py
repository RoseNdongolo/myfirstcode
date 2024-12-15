from rest_framework import serializers
from .models import *

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model=post
        fields='__all__'

