from django.db import models

# Create your models here.

class KVForm(models.Model):
	description = models.CharField(max_length = 100, blank = False, null = False)
	code = models.CharField(max_length = 15, null = False, blank = False)
	
	def __str__(self):
		return self.description


class KVInstance(models.Model):
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


class KVKey(models.Model):
	kv_type = models.ForeignKey(KVType, null = False, blank = False, on_delete = models.CASCADE)
	kv_form = models.ForeignKey(KVForm, null = False, blank = False, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100, null = False, blank = False)
	null = models.BooleanField(null = False, blank = False, default = False)
	blank = models.BooleanField(null = False, blank = False, default = False)
	default = models.CharField(max_length = 100, null = True, blank = True)
	help_text = models.CharField(max_length = 500, null = True, blank = True)
	
	def __str__(self):
		return self.name


class KVValue(models.Model):
	kv_key = models.ForeignKey(KVKey, null = False, blank = False, on_delete = models.CASCADE)
	kv_instance = models.ForeignKey(KVInstance, null = False, blank = False, on_delete = models.CASCADE)
	value_integer = models.IntegerField(default = None, null = True, blank = True)
	value_boolean = models.NullBooleanField(default = None, null = True, blank = True)
	value_text = models.TextField(default = '', null = True, blank = True)
	value_float = models.FloatField(default = None, null = True, blank = True)
	value_file = models.FloatField(default = None, null = True, blank = True)
	value_choice = models.CharField(max_length = 100, default = '', null = True, blank = True)
	value_datetime = models.DateTimeField(default = None, null = True, blank = True)
	updated_at = models.DateTimeField(auto_now = True)
	created_at = models.DateTimeField(auto_now_add = True)