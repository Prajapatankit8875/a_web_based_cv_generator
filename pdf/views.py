from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        summary = request.POST["summary"]
        degree = request.POST["degree"]
        school = request.POST["school"]
        university = request.POST["university"]
        experience = request.POST["experience"]
        skills = request.POST["skills"]
        projects = request.POST["projects"]

        profile = Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,experience=experience,skills=skills,projects=projects)
        profile.save()

    
    return render(request,'pdf/accept.html')

def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile':user_profile})
    options = {
        'page-size':'letter',
        'encoding':"UTF-8",
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Dispodition'] = 'attachment'
    filename = 'resume.pdf'
    return response

def list (request):
    profiles = Profile.objects.all()
    return render(request,'pdf/list.html',{'profiles':profiles})







