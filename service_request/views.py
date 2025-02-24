from django.shortcuts import render, redirect
from . models import Service

# Create your views here.
def uservice(request):
    if request.method == "POST":
        name = request.POST['nm']
        srt = request.POST['srt']
        sd = request.POST['sd']
        img = request.FILES['img']
        Service.objects.create(name=name, stype=srt, description=sd, image = img)
    return render(request, 'user.html')

def tr(request):
    ssr = Service.objects.all()
    return render(request, 'tr.html', {'sr':ssr})


def cs(request):
    ssr = Service.objects.all()
    return render(request, 'usersup.html', {'sr':ssr})

def detail(request, id):
    details = Service.objects.get(id = id)
    if request.method == "POST":
        details.comment = request.POST['comm']
        details.status = request.POST['stat']
        details.save()
        return redirect('cs')
    return render(request, 'sdetail.html', {'details' : details})