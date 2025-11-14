"""
URL configuration for quiz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from authentication.views import signup_view,login_view,logout_view
from quizapp.views import dashboard_view,quizform_view,myquizzes_view,profile_view,takequiz_view,result_view
from quizapp.views import analytics_views
from quizapp.views import allquiz_views,delete_quiz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup_view,name='signup'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('',dashboard_view,name='dashboard'),
    path('form/',quizform_view,name='quizform'),
    path('myquiz/',myquizzes_view,name = 'myquiz'),
    path('profile/',profile_view,name='profile'),
    path('quiz/<int:quiz_id>/',takequiz_view,name='takequiz'),
    path('result/<int:quiz_id>/',result_view,name='result'),
    path('analytics/',analytics_views,name='analytics'),
    path('allquiz/',allquiz_views,name='allquiz'),
    path('delete_quiz/<int:quiz_id>/',delete_quiz,name='deletequiz')
    
]
