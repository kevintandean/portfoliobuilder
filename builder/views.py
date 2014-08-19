import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from jfu.http import upload_receive
from builder.models import Text, Project


def edit(request):
    project = Project.objects.filter(user=request.user)
    # angular_model =
    return render(request,'freelancer/index.html', {'project':project})

@csrf_exempt
def update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print data
        for key in data:
            # print key
            # Text.objects.get_or_create(user=request.user.id, html_id=key)
            # print ("created")
            try:
                text = Text.objects.get(user=request.user.id, html_id=key)
            except Text.DoesNotExist:
                text = Text.objects.create(user=request.user, html_id=key)


            text.text = data[key]
            text.save()
    return

@csrf_exempt
def newproject(request):
    if request.method == 'GET':
        project = [Project.objects.create(user=request.user)]
        thumbnail = render(request,'freelancer/include/portfolio_thumbnail.html', {'project':project})
        return thumbnail

@csrf_exempt
def newproject_modal(request, project_id):
    project = [Project.objects.get(id=project_id)]
    return render(request, 'freelancer/include/portfolio_modal.html', {'project':project})

@csrf_exempt
def delete_project(request, project_id):
    Project.objects.get(id=project_id).delete()
    print "deleted"

@csrf_exempt
@login_required
def upload(request, project_id):
    # file = upload_receive(request)
    print request.FILES
    instance = Project.objects.get(id=project_id)
    instance.image = request.FILES['file']
    instance.save()
    image_url = {'image_url':instance.image.url}
    print "yeay"
    # return render(request, 'freelancer/include/imageupload.html',{'proj':instance})
    return HttpResponse(json.dumps(image_url), content_type='application/json')

