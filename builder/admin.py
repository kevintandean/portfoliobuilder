from django.contrib import admin

# Register your models here.
from builder.models import *

admin.site.register(Text)
admin.site.register(TextArea)
admin.site.register(Image)
admin.site.register(Project)
admin.site.register(Color)
