from django.contrib import admin
from django.urls import path
from kvtest_app.views import TestView

urlpatterns = [
	path('test/', TestView.as_view()),
	path('admin/', admin.site.urls),
]
