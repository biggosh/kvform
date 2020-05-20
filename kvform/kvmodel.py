from django.db import models
from datetime import datetime
from kvform.models import KVKey, KVForm, KVInstance, KVValue


class KVModelMetaclass(type):
	
	def __refresh_fields__(new_class, model_name):
		if model_name is not None:
			new_class._meta.concrete_fields = []
			new_class._meta.fields = []
			new_class._meta.mandatory_fields = []
			new_class._meta.fields_field_type = {}
			
			new_class.model = KVForm.objects.filter(code = model_name)[0]

			# retrieve all fields for the specified model/form
			fields = KVKey.objects.filter(kv_form__code = model_name)
			for f in fields:
				key_type = f.kv_type.django_type
				tmp_field = None
				if key_type:
					if key_type == "CharField":
						tmp_field = models.CharField(max_length = 100, null = f.null, blank = f.blank, name = f.name)
						new_class._meta.fields_field_type.update({f.name: 'text'})
						
					if key_type == "IntegerField":
						tmp_field = models.IntegerField(null = f.null, blank = f.blank, name = f.name)
						new_class._meta.fields_field_type.update({f.name: 'integer'})
						
					if key_type == "FloatField":
						tmp_field = models.FloatField(null = f.null, blank = f.blank, name = f.name)
						new_class._meta.fields_field_type.update({f.name: 'float'})
						
					if key_type == "BooleanField":
						tmp_field = models.BooleanField(null = f.null, blank = f.blank, name = f.name)
						new_class._meta.fields_field_type.update({f.name: 'boolean'})
						
					if key_type == "NullBooleanField":
						tmp_field = models.BooleanField(null = f.null, blank = f.blank, name = f.name)
						new_class._meta.fields_field_type.update({f.name: 'boolean'})
						
				if tmp_field:
					new_class._meta.concrete_fields.append(tmp_field)
					new_class._meta.fields.append(tmp_field)
					if f.null == False:
						new_class._meta.mandatory_fields.append(tmp_field)
						

	def __new__(mcs, name, bases, attrs):
		new_class = super(KVModelMetaclass, mcs).__new__(mcs, name, bases, attrs)
		new_class.__refresh_fields__ = mcs.__refresh_fields__
		
		model_name = new_class.get_model_name()
		mcs.__refresh_fields__(new_class, model_name)
		
		return new_class
		

class KVModel(metaclass=KVModelMetaclass):
	"""
	Logical model is converted into physical model by this class
	"""

	model_name = None
	unique_key = None
	
	
	def full_clean(self, exclude, validate_unique):
		pass


	def get_unique_key(self):
		if self.unique_key:
			return self.unique_key
		else:
			return(datetime.now().strftime("%Y%m%d%H%M%S%f"))

	def save(self, commit = True):
		"""
		Must manage a creation of a key
		Must manage an update of a form
		
		:param commit:
		:return:
		"""		
		
		if not self.unique_key:
			# unique_key == None => new instance and creation of new kvvalue entries
			instance = KVInstance()
			instance.key = self.get_unique_key()
			instance.kv_form = self.model
			instance.save()
			
			fields = KVKey.objects.filter(kv_form__code = self.model.code)
			for f in fields:
				field_type = self._meta.fields_field_type[f.name]
				value = getattr(self, f.name)
				tmp_value = KVValue()
				tmp_value.kv_key = f
				tmp_value.kv_instance = instance
				
				if field_type == "text":
					tmp_value.value_text = value
				if field_type == "integer":
					tmp_value.value_integer = value
				if field_type == "boolean"	:
					tmp_value.value_boolean = value
				if field_type == "float":
					tmp_value.value_float = value
				
				tmp_value.save()
			
		else:
			# update the already existent instance
			pass
		
		for f in self._meta.fields:
			value = getattr(self, f.name)			
			s = f'{f.name}: {value} --> {self._meta.fields_field_type[f.name]}'
			print(s)


	def validate_unique(self, exclude):
		pass
	
	
	@classmethod
	def get_model_name(cls):
		return cls.model_name



	# TODO
	def __repr__(self):
		return "KVModel " + self.model_name
	
	def __str__(self):
		return "KVModel " + self.model_name
	
	def __unicode__(self):
		return "KVModel " + self.model_name
	
	class _meta:
		private_fields = []
		many_to_many = []
