import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Students
from .serializerStudents import StudentsSerializer
 


# Create your views here.
@api_view(['GET'])
def get_students(request: Request):
    students = Students.objects.all()
    serializerData = StudentsSerializer(students, many=True)
    return Response(serializerData.data, status=status.HTTP_200_OK)
@api_view(['GET'])
def get_student_details(request: Request, pk):
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    serializerData = StudentsSerializer(student)
    return Response(serializerData.data, status=status.HTTP_200_OK)
@api_view(['POST'])
def create_student(request: Request):
    email               = request.data.get('email')
    password            = request.data.get('password')
    firstname           = request.data.get('firstname')
    lastname            = request.data.get('lastname')
    dob                 = request.data.get('dob')
    age                 = request.data.get('age')
    single              = request.data.get('single')
    photo               = request.data.get('photo')
    emailpattern        = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    passwordpattern     = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if not re.match(emailpattern, email):
        return Response({'error': 'Invalid email format.'}, status=status.HTTP_402_PAYMENT_REQUIRED)
    if not re.search(passwordpattern, password):
        return Response({'error': 'Password must be strong.'}, status=status.HTTP_403_FORBIDDEN)
    if firstname is None or firstname.strip() == "":
        return Response({'error': 'First name cannot be empty.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if lastname is None or lastname.strip() == "":
        return Response({'error': 'Last name cannot be empty.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if dob is None:
        return Response({'error': 'Date of Birth is required.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if single is None:
        return Response({'error': 'single status is required.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if age < 0 or age > 100:
        return Response({'error': 'age must be between 0 and 100.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if Students.objects.filter(email=email).exists():
        return Response({'error': 'Email already exists.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    data=request.data
    serializer = StudentsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def update_student(request: Request, pk):
   email           = request.data.get('email')
   password        = request.data.get('password')
   firstname       = request.data.get('firstname')
   lastname        = request.data.get('lastname')
   dob             = request.data.get('dob')
   age             = request.data.get('age')
   single          = request.data.get('single')
   photo           = request.data.get('photo')
   emailpattern    = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
   passwordpattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
   if not re.match(emailpattern, email):
       return Response({'error': 'Invalid email format.'}, status=status.HTTP_402_PAYMENT_REQUIRED)
   if not re.search(passwordpattern, password):
       return Response({'error': 'Password must be strong.'}, status=status.HTTP_403_FORBIDDEN)
   if firstname is None or firstname.strip() == "":
       return Response({'error': 'First name cannot be empty.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
   if lastname is None or lastname.strip() == "":
       return Response({'error': 'Last name cannot be empty.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
   if dob is None:
       return Response({'error': 'Date of Birth is required.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
   if single is None:
       return Response({'error': 'Single status is required.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
   if age < 0 or age > 100:
       return Response({'error': 'age must be between 0 and 100.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
   
   try:
       student = Students.objects.get(pk=pk)
   except Students.DoesNotExist:
       return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
   
   serializer = StudentsSerializer(student, data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_200_OK)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_student(request: Request, pk):
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['POST'])
def login_student(request: Request):
    email       = request.data.get('email')
    password    = request.data.get('password')
    try:
        student = Students.objects.get(email=email, password=password)
    except Students.DoesNotExist:
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_404_NOT_FOUND)
    serializerData = StudentsSerializer(student)
    return Response(serializerData.data, status=status.HTTP_200_OK)
