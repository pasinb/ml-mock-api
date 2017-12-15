from rest_framework import serializers
from .models import *

class ScmUserSerializer(serializers.ModelSerializer):
    class Meta():
        model = ScmUser
        fields = ('__all__')
