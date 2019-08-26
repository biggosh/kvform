from django.contrib import admin
from kvform.models import KVType, KVKey, KVForm, KVValue, KVInstance

# Register your models here.

admin.site.register(KVType)
admin.site.register(KVForm)
admin.site.register(KVKey)
admin.site.register(KVValue)
admin.site.register(KVInstance)