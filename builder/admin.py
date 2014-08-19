from django.contrib import admin

# Register your models here.
from builder.models import Text, TextArea, Image, Project

admin.site.register(Text)
admin.site.register(TextArea)
admin.site.register(Image)
admin.site.register(Project)
