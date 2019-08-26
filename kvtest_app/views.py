from django.forms import ModelForm
from kvform import kvmodel
from django.views.generic import CreateView
from django.forms.utils import ErrorList
from kvform.models import KVType

class TestModel(kvmodel.KVModel):
	model_name = 'PROFILE'


class TestForm(ModelForm):
	class Meta:
		model = TestModel
		fields = '__all__'
		# model = KVType
		# fields = ['code', 'description', ]
		

class TestView(CreateView):
	template_name = 'test.html'
	form_class = TestForm
	success_url = '/test/'
