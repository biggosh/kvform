from django.forms import ModelForm
from kvform.kvforms import KVForm
from kvform import kvmodel


class TestModel(kvmodel.KVModel):
	model_name = 'PROFILE'


class TestForm(KVForm):
	class Meta:
		model = TestModel
		fields = '__all__'
	# model = KVType
	# fields = ['code', 'description', ]
