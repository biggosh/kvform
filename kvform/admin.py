from django.contrib import admin
from kvform.models import KVType, KVField, KVModelName, KVValue, KVRecord

# Register your models here.

admin.site.register(KVType)
admin.site.register(KVModelName)
admin.site.register(KVField)
admin.site.register(KVValue)
admin.site.register(KVRecord)
