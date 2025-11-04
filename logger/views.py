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

from datetime import datetime

@api_view(['GET'])
def getloggerbyhospitalid(request, id):
    try:
        Hosp = Hospitals.objects.get(gid=id)
    except Hospitals.DoesNotExist:
        return Response({"error": "Hospital not found"}, status=404)

    # Get all loggers for the hospital
    logger_qs = Logger.objects.filter(
        hosp_id=Hosp
    ).exclude(visited_time__isnull=True).exclude(visited_time="null")

    serializer = LoggerSerializer(logger_qs, many=True)
    logger_data = serializer.data

    # Debug: print all raw visited_time strings
    print("Before sorting:")
    for i in logger_data:
        print(i['visited_time'])

    # Correct format: day/month/year
    def parse_visited_time(item):
        try:
            return datetime.strptime(item['visited_time'], "%d/%m/%Y, %I:%M:%S %p")
        except Exception as e:
            print(f"Date parse error for {item['visited_time']}: {e}")
            return datetime.min  # Push unparseable items to the end

    # Sort logger list by datetime DESC (most recent first)
    logger_sorted = sorted(logger_data, key=parse_visited_time, reverse=True)

    # Map user_id to user_name
    user_map = {u['id']: u['name'] for u in user.objects.values('id', 'name')}
    for entry in logger_sorted:
        uid = entry.get('user_id')
        entry['user_name'] = user_map.get(uid, "Unknown")

    print("After sorting:")
    for i in logger_sorted:
        print(i['visited_time'])

    return Response(logger_sorted)

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

            
     