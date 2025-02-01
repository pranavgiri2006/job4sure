"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from development import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loadhomepage, name='home.html'),
    path('loadhome', views.loadhome),
    path('loadhomepage', views.loadhome),
    path('loadhomepro', views.homepro),
    path('loadhomeseek', views.homeseek),
    path('loadsignup',views.loadsignup),
    path('signupaction',views.signupaction),
    path('loginjpaction',views.loginjpaction),
    path('loginjsaction',views.loginjsaction),
    # path('loadlogin',views.loadlogin),
    # path('loginaction',views.loginaction),
    path('loadprofileinfopro', views.profileinfopro),
    path('loadprofileinfoseek', views.profileinfoseek),
    path('profileproviderurl',views.profileprovider),
    path('profileseekerurl',views.profileseeker),
    path('loadupload',views.upload),
    path('uploadaction',views.uploadaction),
    path('loadjp',views.loadjp),
    path('loadjs',views.loadjs),
    path('loadnotificationpro',views.notificationpro),
    path('loadnotificationseek', views.notificationseek),
    path('loadfeedback',views.loadfeedback),
    path('loadfeedback', views.feedback),
    path('loadcomplain', views.loadcomplain),
    path('complainurl', views.complain),
    path('viewscomplain',views.viewcomplain),
    path('complainact', views.complainactcode),
    path('viewsfeedback',views.viewfeedback),
    path('viewsfeedback', views.feedbackurl),
    path('loadjobinfo',views.jobinfo),
    path('viewsjoburl', views.jobinfourl),
    path('loadcontact',views.loadcontactcode),
    path('contacturl',views.contacturl),
    path('loadsearchjob',views.searchjob),
    path('loadsettingseeker', views.settingseeker),
]

