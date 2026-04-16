from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, Application

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


def job_detail(request, id):
    job = get_object_or_404(Job, id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        resume = request.FILES.get("resume")

        Application.objects.create(
            job=job,
            name=name,
            email=email,
            phone=phone,
            resume=resume
        )

        return redirect('job_list')

    return render(request, 'jobs/job_detail.html', {'job': job})