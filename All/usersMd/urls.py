from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginView, SignupView,SignoutView, CreateWork,GetWorks,GetAllUsers,GetAllWorks,DeleteWork,DeleteWorkasManager,GetCredentials,ToggleUsersManagerRole

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('signup', SignupView.as_view(), name='signup'),
    path('signout', SignoutView.as_view(), name='signout'),

    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),  # rest framework refresh hazır endpoint.
    
    path('work/create', CreateWork.as_view(), name='create_work'),  
    path('work/get', GetWorks.as_view(), name='get_work'),  
    path('work/getall', GetAllWorks.as_view(), name='getall_work'),  
    path('users/getall', GetAllUsers.as_view(), name='getall_users'),  
    path('users/get', GetCredentials.as_view(), name='get_user'),  
    path('users/toggle', ToggleUsersManagerRole.as_view(), name='toggle_user'),  
    path('work/delete', DeleteWork.as_view(), name='delete_work'),  
    path('work/forcedelete', DeleteWorkasManager.as_view(), name='delete_asMan_work'),  

]

"""
pre-documentation : 
...com/api/ :

example signup --- "signup"
post:
{
    "username": "testuser",
    "email": "test@test.com",
    "first_name": "test",
    "last_name": "tetes",
    "password": "Apple14-"
}


example login --- "login"
post:
{
    "email": "test@test.com",
    "password": "Apple14-"
}

example refresh --- "refresh"


example signout --- "signout"
post:
{} //empty json.

example create work --- "work/create"

post:
{
    "company" = "id form",
    "about" = "255 max length",
    "work_hour" = "integer",
    "date" = "YYYY-MM-DD",
}

example delete work --- "work/delete"
{
"id" : 5
}

example delete work as manager--- "work/forcedelete" NEED TO BE MANAGER
{
"id" : 5
}

example getWork --- "work/get"
get:

example getAllWorks --- "work/getall" NEED TO BE MANAGER
post:
{
    ---! all params are optional !---
 "user" : "",
 "company" : "",
 "date" : ""
}

example getAllUsers --- "users/getall" NEED TO BE MANAGER
get:

admin user : o***i@i**d.com
      pass : A***4-

"""