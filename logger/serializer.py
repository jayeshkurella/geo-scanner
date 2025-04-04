from rest_framework import serializers
from .models import Logger,Hospitals,Product,Feedback

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospitals
        fields ='__all__'

class LoggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logger
        fields = '__all__'
        depth=3

class ProductSerializer(serializers.ModelSerializer):
     class Meta:
          model = Product
          fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
     class Meta:
          model = Feedback
          fields = '__all__'
          


         
