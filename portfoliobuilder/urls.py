from django.contrib import admin
from tastypie.api import Api
from builder.api.resources import TextResource, TextAreaResource, ImageResource, UserResource

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

admin.autodiscover()

v1_api = Api(api_name="v1")
v1_api.register(UserResource())
v1_api.register(TextResource())
v1_api.register(TextAreaResource())
v1_api.register(ImageResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portfoliobuilder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    # url(r'api/doc/',
    # include('tastypie_swagger.urls', namespace='tastypie_swagger'),
    # kwargs={"tastypie_api_module": "v1_api",
    #         "namespace": "tastypie_swagger"}
# ),
    url(r'^edit/$', 'builder.views.edit', name='edit'),
    url(r'^update/$', 'builder.views.update', name='update'),
    url(r'^newproject/$', 'builder.views.newproject', name='newproject'),
    # url(r'^newproject_modal/$', 'builder.views.newproject_modal', name='newproject_modal'),
    url(r'^newproject_modal/(?P<project_id>\w+)/$', 'builder.views.newproject_modal', name="newproject_modal"),
    url(r'^delete_project/(?P<project_id>\w+)/$', 'builder.views.delete_project', name="newproject_modal"),
    url( r'upload/(?P<project_id>\w+)/$', 'builder.views.upload', name = 'jfu_upload' ),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
