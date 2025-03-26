from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status
from .serializers import UserSerializer, WorkSerializer
from .models import Work,User

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

from rest_framework.permissions import IsAuthenticated, BasePermission
class IsManager(BasePermission):
    def has_permission(self, request):
        return request.user and request.user.isManager


class LoginView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')

        # Kullanıcıyı authenticate et
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # JWT token oluştur
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # Token'ları cookie olarak gönder
            response = Response({
                'message': 'Giriş başarılı',
                'user_id': user.id,
                'email': user.email,
            })
            response.set_cookie('access_token', access_token, httponly=True, secure=False, samesite='None')
            response.set_cookie('refresh_token', refresh_token, httponly=True, secure=False, samesite='None')
            return response
        else:
            return Response({'message': 'Geçersiz kimlik bilgileri'}, status=400)

class GetCredentials(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.COOKIES)
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Kullanıcıyı kaydet
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SignoutView(APIView):
    def post(self, request):
        response = Response({'message': 'Çıkış Yapıldı'})
        response.cookies.clear()
        return response
    
class CreateWork(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Serializer'a ekstra bilgi (request.user) geç
        serializer = WorkSerializer(data=request.data, context={'user': request.user})
        
        if serializer.is_valid():
            serializer.save()  # Serializer'ın save() metodunda user'ı kullanabilirsiniz
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteWork(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request) : 

        try:
            work = Work.objects.get(id = request.data.get("id"))
            if not work or work == "" :
                return Response({"message" : "please specify the id of the work to be deleted as 'id' : 5;"},status=400)
            if work.user == request.user : 
                work.delete()
                return Response({"message" : "deleted"})
            else : 
                raise AuthenticationFailed("User does not owns the work")
        except Work.DoesNotExist:
            return Response({"message" : "task does not exists"},status=404)
       
class DeleteWorkasManager(APIView):
    permission_classes = [IsAuthenticated,IsManager]
    def post(self,request) : 
        try:

            work = Work.objects.get(id = request.data.get("id"))
            if not work or work == "" :
                return Response({"message" : "please specify the id of the work to be deleted as 'id' : 5;"},status=400)
            work.delete()
            return Response({"message" : "deleted"})

        except Work.DoesNotExist:
            return Response({"message" : "task does not exists"},status=404)

class GetWorks(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        work_query = Work.objects.filter(user=request.user)
        serializer = WorkSerializer(work_query, many=True)
        return Response(serializer.data)

class GetAllWorks(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    def post(self, request):
        filter_params = {}

        # Boş stringler yerine None kontrolü eklenmiş
        wanted_user = request.data.get("wanted_user")
        if wanted_user and wanted_user != "":
            filter_params["user"] = wanted_user

        wanted_company = request.data.get("wanted_company")
        if wanted_company and wanted_company != "":
            filter_params["company"] = wanted_company

        wanted_date = request.data.get("wanted_date")
        if wanted_date and wanted_date != "":
            filter_params["date"] = wanted_date

        try:
            work_query = Work.objects.filter(**filter_params)
            serializer = WorkSerializer(work_query, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message": f"Error occurred: {e}"}, status=500)

class GetAllUsers(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    def get(self,request):
        user_query = User.objects.all()
        serializer = UserSerializer(user_query,many = True)

        return Response(serializer.data)
        





"""
pre-documentation : 

example signup ---
post:
{
    "username": "testuser",
    "email": "test@test.com",
    "first_name": "test",
    "last_name": "tetes",
    "password": "Apple14-"
}


example login ---
post:
{
    "email": "test@test.com",
    "password": "Apple14-"
}

example signout ---
post:
{} //empty json.

example create work ---

post:
{
    "company" = "id form",
    "about" = "255 max length",
    "work_hour" = "integer",
    "date" = "YYYY-MM-DD",
}

example delete work ---
{
"id" : 5
}

example delete work as manager---
{
"id" : 5
}

example getWork ---
get:

example getAllWorks ---
post:
{
    ---! all params are optional !---
 "user" : "",
 "company" : "",
 "date" : ""
}

example getAllUsers ---
get:

admin user : o***i@i**d.com
      pass : A***4-

"""