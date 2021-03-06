"""django_kvform URL Configuration

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
from kvtest_app.views import TestView

urlpatterns = [
	path('test/', TestView.as_view()),
    path('admin/', admin.site.urls),
]


from django.db.models.signals import post_save
from django.dispatch import receiver
from kvform.models import KVKey

@receiver(post_save, sender=KVKey)
def handle_refresh_fields(sender, **kwargs):	
	print("RECEIVER: " + str(sender))
	print(kwargs)
