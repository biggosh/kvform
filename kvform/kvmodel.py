from django.db import models
# from kvform import models
from kvform.models import KVKey, KVForm


class KVModelMetaclass(type):
	def __new__(mcs, name, bases, attrs):
		new_class = super(KVModelMetaclass, mcs).__new__(mcs, name, bases, attrs)
		
		model_name = new_class.get_model_name()
		
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
		
		return new_class
		

class KVModel(metaclass=KVModelMetaclass):
	"""
	Logical model is converted into physical model by this class
	"""

	model_name = None

	def full_clean(self, exclude, validate_unique):
		pass


	def save(self, commit = True):
		"""
		Must manage a creation of a key
		Must manage an update of a form
		
		:param commit:
		:return:
		"""
		for f in self._meta.fields:
			value = getattr(self, f.name)
			print(f.name + ": " + str(value))
            

	def validate_unique(self, exclude):
		pass
	
	
	@classmethod
	def get_model_name(cls):
		return cls.model_name



	# da capire quale implementare
	def __repr__(self):
		return "KVModel " + self.model_name
	
	def __str__(self):
		return "KVModel " + self.model_name
	
	def __unicode__(self):
		return "KVModel " + self.model_name
	
	class _meta:
		private_fields = []
		many_to_many = []
	