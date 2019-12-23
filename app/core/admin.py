from django.contrib import admin
from core import models

# Register your models here.
admin.site.register(models.Brand)
admin.site.register(models.Processor)
admin.site.register(models.Motherboard)
admin.site.register(models.Memory)
admin.site.register(models.GraphicCard)
