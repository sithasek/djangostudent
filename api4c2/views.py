import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from api4c2.models import Student4c2
from api4c2.serializerStudent4c2 import Student4c2Serializer

@api_view(['GET', 'POST'])
def student4c2_list_create(request: Request) -> Response:
    
    email       = request.data.get('email')
    password    = request.data.get('password')
    name        = request.data.get('name')
    dob         = request.data.get('dob')
    session     = request.data.get('session')
    hobbies     = request.data.get('hobbies')
    score       = request.data.get('score')
    status_value = request.data.get('status')
    gender      = request.data.get('gender')
    emailpattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    passwordpattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    
    if request.method == 'GET':
        students = Student4c2.objects.all()
        serializer = Student4c2Serializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if not re.match(emailpattern, request.data.get('email', '')):
            return Response({'error': 'Invalid email format.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if not re.search(passwordpattern, password):
            return Response({'error': 'Password must be strong.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        if session not in ['Morning', 'Afternoon', 'Evening']:
            return Response({'error': 'Session must be Morning, Afternoon, or Evening.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if hobbies is None or hobbies.strip() == "":
            return Response({'error': 'Hobbies cannot be empty.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        if dob is None or dob.strip() == "":
            return Response({'error': 'Date of Birth is required.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        if name is None or name.strip() == "":
            return Response({'error': 'Name cannot be empty.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if gender not in ['Male', 'Female']:
            return Response({'error': 'Gender must be Male, Female'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if score < 0 or score > 100:
            return Response({'error': 'Score must be between 0 and 100.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if status_value not in ['Single', 'Maried']:
            return Response({'error': 'Status must be Single or Maried.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if Student4c2.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists.'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = Student4c2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_student4c2(request: Request) -> Response:
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        student = Student4c2.objects.get(email=email, password=password)
        serializer = Student4c2Serializer(student)
        return Response(serializer.data)
    except Student4c2.DoesNotExist:
        return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET', 'PUT', 'DELETE'])
def student4c2_detail(request: Request, pk: int) -> Response:
    email       = request.data.get('email')
    password    = request.data.get('password')
    name        = request.data.get('name')
    dob         = request.data.get('dob')
    session     = request.data.get('session')
    hobbies     = request.data.get('hobbies')
    score       = request.data.get('score')
    status_value = request.data.get('status')
    gender      = request.data.get('gender')
    emailpattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    passwordpattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    try:
        student = Student4c2.objects.get(pk=pk)
    except Student4c2.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Student4c2Serializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if not re.match(emailpattern, request.data.get('email', '')):
            return Response({'error': 'Invalid email format.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if not re.search(passwordpattern, password):
            return Response({'error': 'Password must be strong.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        if session not in ['Morning', 'Afternoon', 'Evening']:
            return Response({'error': 'Session must be Morning, Afternoon, or Evening.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if hobbies is None or hobbies.strip() == "":
            return Response({'error': 'Hobbies cannot be empty.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        if dob is None:
            return Response({'error': 'Date of Birth is required.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        if name is None or name.strip() == "":
            return Response({'error': 'Name cannot be empty.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if gender not in ['Male', 'Female']:
            return Response({'error': 'Gender must be Male, Female, or Other.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if score < 0 or score > 100:
            return Response({'error': 'Score must be between 0 and 100.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if status_value not in ['Single', 'Maried']:
            return Response({'error': 'Status must be Single or Maried.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        #if Student4c2.objects.filter(email=email).exists():
        #    return Response({'error': 'Email already exists.'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = Student4c2Serializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

