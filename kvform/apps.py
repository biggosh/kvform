from django.apps import AppConfig
from django.db.model.signals import post_save
from django.dispatch import receiver
from kvform.models import KVKey


class KvformConfig(AppConfig):
    name = 'kvform'
	
	def ready(self):
		import kvform.signals
