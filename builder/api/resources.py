from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.cache import SimpleCache
from tastypie.constants import ALL_WITH_RELATIONS
from tastypie.fields import ToManyField, ToOneField

__author__ = 'kevin'
from tastypie.resources import ModelResource
from builder.models import *

# If you put this at the end of the file, you wouldn't have to put the full path to each resource in a string
class UserResource(ModelResource):
    text = ToManyField('builder.api.resources.TextResource', 'user_text', full=True)
    textarea = ToManyField('builder.api.resources.TextAreaResource', 'user_textarea', full=True)
    image = ToManyField('builder.api.resources.ImageResource', 'user_image', full=True)
    project = ToManyField('builder.api.resources.ProjectResource', 'user_project', full=True)


    class Meta:
        format = 'json'
        queryset = User.objects.all()
        resource_name = "user"
        ordering = ['first_name', 'last_name']
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'delete', 'put', 'patch']

        # cache = SimpleCache(60)

class TextResource(ModelResource):
    class Meta:
        format = 'json'
        queryset = Text.objects.all()
        resource_name = 'text'

class TextAreaResource(ModelResource):
    class Meta:
        format = 'json'
        queryset = TextArea.objects.all()
        resource_name = 'text'

class ImageResource(ModelResource):
    class Meta:
        format = 'json'
        queryset = Image.objects.all()
        resource_name = 'text'

class ProjectResource(ModelResource):
    class Meta:
        format = 'json'
        queryset = Project.objects.all()
        resource_name = 'project'
