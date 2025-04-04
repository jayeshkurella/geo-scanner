from django.shortcuts import render
from rest_framework import viewsets
from .models import Logger,Hospitals,Product,Feedback
from registration.models import user
from .serializer import LoggerSerializer,HospitalSerializer,ProductSerializer,FeedbackSerializer
from registration.serializers import UsersSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.db.models import F
# Create your views here.
class post_visited_details(viewsets.ModelViewSet):
    queryset = Logger.objects.all()
    serializer_class = LoggerSerializer
        
    def create(self, request, *args, **kwargs):
        Logger_data = request.data  
        print(request.data)
        print(request.data)
        create_user = Logger(
            hosp=Hospitals.objects.get(gid=Logger_data["hosp_id"]),
            visited_time = Logger_data['visited_time'],
            user = user.objects.get(id=Logger_data["user_id"])
           

            )
        
        print("hospihhhhhhhhhhhhhhhhhhh",create_user)
        create_user.save()
        
        # print(create_user)
        serializer = LoggerSerializer(create_user)
        return Response(serializer.data)

import datetime
##get two tables data by hospital id (logger/Hospital)
@api_view(['GET'])
def getloggerbyhospitalid(request, id):
   
    Hosp = Hospitals.objects.get(gid=id)
    print("hospital id is",Hosp)
    logger = Logger.objects.exclude(hosp_id__isnull=True).exclude(visited_time__exact="null").filter(hosp_id=Hosp).order_by('-visited_time')
    print("logger details is",logger)
    serializer = LoggerSerializer(logger, many=True)
    # for data in serializer.data:
    #     if data['visited_time'] == "null":
    #         del data['visited_time']

    
    users = user.objects.values('id', 'name')  # Modify 'name' to the actual field name in your registration_user model
    user_data = {user['id']: user['name'] for user in users}

    for data in serializer.data:
        user_id = data.get('user_id')
        if user_id in user_data:
            data['user_id'] = user_id
            data['user_name'] = user_data[user_id]
    return Response(serializer.data)
    # return Response(serializer.dat

##get logger data by uuid
@api_view(['GET'])
def getloggerbyloggerid(request,id):
    logger=Logger.objects.get(logger=id)
    serializer = LoggerSerializer(logger)
    return Response(serializer.data)

##update logger details
## update only two fields
@api_view(['PUT'])
def putloggerdetails(request,id):
    data = request.data
    logger = Logger.objects.get(logger=id)
    logger.description = data['description']
    logger.status = data['status']
    logger.save()
    serializer = LoggerSerializer(logger)
    return Response(serializer.data)

##post hospital product details
class post_hospital_product_details(viewsets.ModelViewSet):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
     
     def hospital_product_details(self,request,*args,**kwargs):
          serializer = ProductSerializer(request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          
## get hospital product details by uuid       
@api_view(['GET'])
def gethospitalproductdetails(request,id):
     product = Product.objects.get(product_id=id)
     serializer = ProductSerializer(product)
     return Response(serializer.data)

# post feedback details
class post_feedback_details(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def create(self, request, *args, **kwargs):
        Logger_data = request.data  
        print(request.data)
        print(request.data)
        create_user = Feedback(
            
            user = user.objects.get(id=Logger_data["user_id"]),
            Feedback=Logger_data["Feedback"],
           
            )
        
        print("hospihhhhhhhhhhhhhhhhhhh",create_user)
        create_user.save()
        
        # print(create_user)
        serializer = FeedbackSerializer(create_user)
        return Response(serializer.data)

            
     