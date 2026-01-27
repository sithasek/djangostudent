import re
from .serializerStudenta01 import Studenta01Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Studenta01
# Create your views here.
@api_view(['GET'])
def get_studenta01(request:Request):
    studenta01_data = Studenta01.objects.all().values()
    studenta01_list = list(studenta01_data)
    return Response(studenta01_list, status=status.HTTP_200_OK)
@api_view(['GET'])
def get_studenta01_details(request:Request, pk:int):
    try:
        studenta01 = Studenta01.objects.get(pk=pk)
    except Studenta01.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(studenta01.email, status=status.HTTP_200_OK)
@api_view(['POST'])
def create_studenta01(request:Request):
    email = request.data.get('email')
    password = request.data.get('password')
    firstname = request.data.get('firstname')
    lastname = request.data.get('lastname')
    dob = request.data.get('dob')
    active = request.data.get('active')
    score = request.data.get('score')
    gender = request.data.get('gender')
    photo = request.data.get('photo')
    emailpattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    passwordpattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if not re.match(emailpattern, email):
        return Response({'error': 'Invalid email format.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if not re.search(passwordpattern, password):
        return Response({'error': 'Password must be strong.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if firstname is None or firstname.strip() == "":
        return Response({'error': 'First name cannot be empty.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if lastname is None or lastname.strip() == "":
        return Response({'error': 'Last name cannot be empty.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if dob is None:
        return Response({'error': 'Date of Birth is required.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if active is None:
        return Response({'error': 'Active status is required.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if score < 0 or score > 100:
        return Response({'error': 'Score must be between 0 and 100.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if  gender not in ['Male', 'Female']:
        return Response({'error': 'Gender must be Male or Female.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if Studenta01.objects.filter(email=email).exists():
        return Response({'error': 'Email already exists.'}, status=status.HTTP_403_FORBIDDEN)
    serializer = Studenta01Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_studenta01(request:Request, pk:int): 
    email = request.data.get('email')
    password = request.data.get('password')
    firstname = request.data.get('firstname')
    lastname = request.data.get('lastname')
    dob = request.data.get('dob')
    active = request.data.get('active')
    score = request.data.get('score')
    gender = request.data.get('gender')
    photo = request.data.get('photo')
    emailpattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    passwordpattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if not re.match(emailpattern, email):
        return Response({'error': 'Invalid email format.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if not re.search(passwordpattern, password):
        return Response({'error': 'Password must be strong.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if firstname is None or firstname.strip() == "":
        return Response({'error': 'First name cannot be empty.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if lastname is None or lastname.strip() == "":
        return Response({'error': 'Last name cannot be empty.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if dob is None:
        return Response({'error': 'Date of Birth is required.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if active is None:
        return Response({'error': 'Active status is required.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if score < 0 or score > 100:
        return Response({'error': 'Score must be between 0 and 100.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if  gender not in ['Male', 'Female']:
        return Response({'error': 'Gender must be Male or Female.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    serializer = Studenta01Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   
@api_view(['DELETE'])
def delete_studenta01(request:Request, pk:int):
    try:
        studenta01 = Studenta01.objects.get(pk=pk)
    except Studenta01.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    studenta01.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    
    
