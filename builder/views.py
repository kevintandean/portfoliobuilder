import json
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from jfu.http import upload_receive
from builder.forms import Form
from builder.models import Text, Project, Image, Color

# @login_required
def landing(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            user = form.save()
            print (request.POST)
            user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, user)

            return redirect("edit")

    else:
        form = Form()
    return render(request, 'freelancer/registration.html', {'form':form})


def edit(request):
    # This seems a bit hacky if a user hasn't made a site yet, maybe you write a function
    # or have a separate workflow for setting up your portfolio for the first time?
    project = Project.objects.filter(user=request.user)
    if len(project)==0:
        project = [Project.objects.create(user=request.user)]
    # request.user is the same thing that this returns, you can just use request.user
    user = User.objects.get(id=request.user.id)
    # print request.user.id
    disabled = 'false'
    color = Color.objects.get_or_create(user=user)
    if color[1]:
        color[0].color = '#18bc9c'
        color[0].save()
    Image.objects.get_or_create(user=user)
    avatar = Image.objects.get(user=user)
    button = 'View'
    buttonlink = '/'+user.username+'/'
    displaybutton = True
    # print user.color.color
    return render(request,'freelancer/index.html', {'project':project, 'disabled' :disabled, 'avatar':avatar, 'button':button, 'buttonlink':buttonlink, 'displaybutton':displaybutton})

def view_portfolio(request, username):
    user = User.objects.get(username=username)
    project = Project.objects.filter(user=user)
    disabled = 'true'
    avatar = Image.objects.get(user=user)
    button = ""
    buttonlink = ""
    displaybutton = False
    if username == request.user.username:
        displaybutton = True
        button = 'Edit'
        buttonlink = '/edit/'
    return render(request,'freelancer/index.html', {'project':project, 'disabled' :disabled, 'avatar':avatar, 'user':user, 'button':button, 'buttonlink':buttonlink, 'displaybutton':displaybutton})

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
def update_project(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print data
        for key in data:
            project = Project.objects.get(id=key)
            project.description = data[key]['description']
            project.title = data[key]['title']
            project.save()
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

@csrf_exempt
def upload_profile(request):
    instance = Image.objects.get(user=request.user)
    instance.image = request.FILES['file']
    instance.save()
    image_url = {'image_url' : instance.image.url}
    return HttpResponse(json.dumps(image_url), content_type='application/json')

    # user = User.objects.get(request.user)
    # try:
    #     text = Text.objects.get(user=request.user, html_id='profilePicture')
    # except Text.DoesNotExist:
    #     text = Text.objects.create(user=request.user, html_id='profilePicture')


# @csrf_exempt
def color(request):
    # print request.user.id
    # print "hey"
    data = json.loads(request.body)
    print data['color']
    user = User.objects.get(id=request.user.id)
    print "hey"
    color = Color.objects.get(user=user)
    color.color = data['color']
    color.save()
    # color = Color.objects.get(user=request.user)
    # color.color = data['color']

    print "yeay"
    # print "yeay"
