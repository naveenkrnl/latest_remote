from django.contrib import admin
from .models import Subject,Unit,Topic,UnitParts,Related,Topic_Links
# Register your models here.


admin.site.register(Subject)
admin.site.register(UnitParts)
admin.site.register(Unit)
admin.site.register(Topic)
admin.site.register(Topic_Links)
admin.site.register(Related)