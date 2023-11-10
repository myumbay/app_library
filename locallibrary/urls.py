"""
URL configuration for locallibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from principal import views
#from . import views
#from django.conf.urls.defaults import *
from locallibrary.views import current_datetime, hours_ahead
#from principal.views import lista_bebidas
from principal import views as empresa1
urlpatterns = [
    path('time/', current_datetime),
    path('admin/', admin.site.urls),
    path('empresa/', empresa1.lista_bebidas,name = 'empresa'),
    #path('time/plus/(\d{1,2})/', hours_ahead),
   
]
