from kvtest_app.forms import TestForm
from django.views.generic import CreateView
from django.forms.utils import ErrorList


class TestView(CreateView):
	template_name = 'test.html'
	form_class = TestForm
	success_url = '/test/'
