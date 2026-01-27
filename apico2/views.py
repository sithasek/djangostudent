import re
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework import status

from apico2.models import Studentc02
from apico2.serializerstudentco2 import Studentc02Serializer

# Create your views here.

@api_view(['GET'])
def get_studentc02(request: Request):
    studentco2 = Studentc02.objects.all()
    serializerData = Studentc02Serializer(studentco2, many=True)
    return Response(serializerData.data, status=status.HTTP_200_OK)
@api_view(['GET'])
def get_studentco2_details(request: Request, pk):
    try:
        studentco2 = Studentc02.objects.get(pk=pk)
    except Studentc02.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    serializerData = Studentc02Serializer(studentco2)
    return Response(serializerData.data, status=status.HTTP_200_OK)
@api_view(['POST'])
def create_studentco2(request: Request):
    
    patternemail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    patternpassword = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*#?&])[A-Za-z\\d@$!%*#?&]{8,20}$"
    email = request.data.get('email')
    password = request.data.get('password')
    name = request.data.get('name')
    dob = request.data.get('dob')
    active = request.data.get('active')
    score = request.data.get('score')
    gender = request.data.get('gender')
    
    if not re.match(patternemail, email):
        return Response({'error': 'Invalid email format'}, status=status.HTTP_400_BAD_REQUEST)
    if not re.search(patternpassword, password):
        return Response({'error': 'Password must be strong!'}, status=status.HTTP_400_BAD_REQUEST)   
    if name == "":
        return Response({'error': 'Name cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)
    if dob is None:
        return Response({'error': 'Date of Birth cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)
    if active not in [True, False]:
        return Response({'error': 'Active must be a boolean value.'}, status=status.HTTP_400_BAD_REQUEST)
    if not (0 <= int(score) <= 100):
        return Response({'error': 'Score must be between 0 and 100.'}, status=status.HTTP_400_BAD_REQUEST)
    if gender not in ['Male', 'Female']:
        return Response({'error': 'Gender must be Male or Female.'}, status=status.HTTP_400_BAD_REQUEST)
    if email and Studentc02.objects.filter(email=email).exists():
        return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
    
    data=request.data
    serializer = Studentc02Serializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_studentco2(request: Request, pk):
    patternemail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    patternpassword = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*#?&])[A-Za-z\\d@$!%*#?&]{8,20}$"
    email = request.data.get('email')
    password = request.data.get('password')
    name = request.data.get('name')
    dob = request.data.get('dob')
    active = request.data.get('active')
    score = request.data.get('score')
    gender = request.data.get('gender')
    
    if not re.match(patternemail, email):
        return Response({'error': 'Invalid email format'}, status=status.HTTP_400_BAD_REQUEST)
    if not re.search(patternpassword, password):
        return Response({'error': 'Password must be strong!'}, status=status.HTTP_400_BAD_REQUEST)   
    if name == "":
        return Response({'error': 'Name cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)
    if dob is None:
        return Response({'error': 'Date of Birth cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)
    if active not in [True, False]:
        return Response({'error': 'Active must be a boolean value.'}, status=status.HTTP_400_BAD_REQUEST)
    if not (0 <= int(score) <= 100):
        return Response({'error': 'Score must be between 0 and 100.'}, status=status.HTTP_400_BAD_REQUEST)
    if gender not in ['Male', 'Female']:
        return Response({'error': 'Gender must be Male or Female.'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        studentco2 = Studentc02.objects.get(pk=pk)
    except Studentc02.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = Studentc02Serializer(studentco2, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    