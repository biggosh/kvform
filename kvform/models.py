from django.db import models

# Create your models here.

class KVModelName(models.Model):
	description = models.CharField(max_length = 100, blank = False, null = False)
	code = models.CharField(max_length = 15, null = False, blank = False)
	
	def __str__(self):
		return self.description


class KVRecord(models.Model):
	"""
	:Description is a free text describing the form
	:key is a unique identifier for each compiled and saved form
	"""
	kv_form = models.ForeignKey(KVModelName, null = False, blank = False, on_delete = models.CASCADE)
	description = models.CharField(max_length = 100, blank = False, null = False)
	key = models.CharField(max_length = 50, blank = False, null = False)
	
	def __str__(self):
		return self.description
	
class KVType(models.Model):
	django_type = models.CharField(max_length = 50, blank = False, null = False)
	code = models.CharField(max_length = 15, null = False, blank = False)
	description = models.CharField(max_length = 100, blank = False, null = False)
	basic_type = models.CharField(max_length = 15, blank = False, null = False)
	
	def __str__(self):
		return self.django_type


class KVField(models.Model):
	"""
	This class is the replacement for the field type.
	The name key comes from Key-Value databases paradigm
	"""
	kv_type = models.ForeignKey(KVType, null = False, blank = False, on_delete = models.CASCADE)
	kv_model = models.ForeignKey(KVModelName, null = False, blank = False, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100, null = False, blank = False)
	null = models.BooleanField(null = False, blank = False, default = False)
	blank = models.BooleanField(null = False, blank = False, default = False)
	default = models.CharField(max_length = 100, null = True, blank = True)
	help_text = models.CharField(max_length = 500, null = True, blank = True)
	
	def __str__(self):
		return self.name


class KVValue(models.Model):
	kv_key = models.ForeignKey(KVField, null = False, blank = False, on_delete = models.CASCADE)
	kv_instance = models.ForeignKey(KVRecord, null = False, blank = False, on_delete = models.CASCADE)
	value_integer = models.IntegerField(default = None, null = True, blank = True)
	value_boolean = models.BooleanField(default = None, null = True, blank = True)
	value_text = models.TextField(default = '', null = True, blank = True)
	value_float = models.FloatField(default = None, null = True, blank = True)
	value_file = models.FloatField(default = None, null = True, blank = True)
	value_choice = models.CharField(max_length = 100, default = '', null = True, blank = True)
	value_datetime = models.DateTimeField(default = None, null = True, blank = True)
	updated_at = models.DateTimeField(auto_now = True)
	created_at = models.DateTimeField(auto_now_add = True)
