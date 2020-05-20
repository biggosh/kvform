from django.db.models.signals import post_save
from django.dispatch import receiver
from kvform.models import KVKey


# Not used. In case of multiple instances it will not work

@receiver(post_save, sender=KVKey)
def handle_refresh_fields(sender, **kwargs):	
	print("RECEIVER: " + str(sender))
	print(kwargs)