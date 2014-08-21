from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Text(models.Model):
    user = models.ForeignKey(User, related_name = 'user_text')
    html_id = models.CharField(max_length=40)
    text = models.CharField(max_length=500, null=True)

class TextArea(models.Model):
    user = models.ForeignKey(User, related_name = 'user_textarea')
    html_id = models.CharField(max_length=40)
    text = models.TextField(null=True)

class Image(models.Model):
    user = models.ForeignKey(User, related_name = 'user_image')
    html_id = models.CharField(max_length=40)
    image = models.ImageField(upload_to='user_image', null=True)

    def image_url(self):
        if bool(self.image)==False:
            return "/media/img/profile.png"
        else:
            return self.image.url


class Project(models.Model):
    user = models.ForeignKey(User, related_name = 'user_project')
    image = models.ImageField(upload_to='project_image', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, default="title here")
    description = models.TextField(null=True, default = "Description here, lorem ipsum.....")

    def angular_title(self):
        # return 'aaaaaaaaa'
        return '{{ project['+str(self.id)+'].title}}'

    def angular_description(self):
        return '{{ project['+str(self.id)+'].description}}'

    def image_url(self):
        if bool(self.image)==False:
            return "/media/img/portfolio/cabin.png"
        else:
            return self.image.url


class Color(models.Model):
    user = models.OneToOneField(User, related_name='color')
    color = models.CharField(max_length=30, null=True)
