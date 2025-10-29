"""cards_gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import (
    home,
    about_us,
    contact_us,
    testing,
    testing_create_update_delete_data,
    create_team_member,
    get_team_members,
    delete_all_team_members,
    delete_team_member,
    edit_team_member,
    user_login,
    user_logout,
    register_user,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about-us/', about_us, name='about-us'),
    path('contact-us/', contact_us, name='contact-us'),
    path('testing/', testing, name='testing'),
    path('testing2/', testing_create_update_delete_data, name='testing2'),
    path('create-team-member/', create_team_member, name='create_team_member'),
    path('team-members/', get_team_members, name='get_team_members'),
    path('delete-all-team-members/', delete_all_team_members, name='delete_all_team_members'),
    path('delete-team-member/<member_id>/', delete_team_member, name="delete_team_member"),
    path('edit-team-member/<member_id>/', edit_team_member, name='edit_team_member'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('register-user/', register_user, name='register_user'),
]
