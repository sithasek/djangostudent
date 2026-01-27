import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from apico1.serializerStudentc01 import StudentC01Serializer
from .models import Studentc01

@api_view(['GET'])
def get_studentc01(request: Request):
    students = Studentc01.objects.all()
    serializer = StudentC01Serializer(students, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_studentco1_details(request: Request, pk: int):
    try:
        student = Studentc01.objects.get(pk=pk)
    except Studentc01.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentC01Serializer(student)
    return Response(serializer.data)
@api_view(['POST'])
def create_studentco1(request: Request):
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
    if Studentc01.objects.filter(email=email).exists():
        return Response({'error': 'Email already exists.'}, status=status.HTTP_403_FORBIDDEN)
    
    serializer = StudentC01Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def update_studentco1(request: Request, pk: int):
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
    
    try:
        student = Studentc01.objects.get(pk=pk)
    except Studentc01.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentC01Serializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_studentco1(request: Request, pk: int):
    try:
        student = Studentc01.objects.get(pk=pk)
    except Studentc01.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
