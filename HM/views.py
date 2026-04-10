from django.shortcuts import render
from .models import Requirement

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        company = request.POST.get("company")
        phone = request.POST.get("phone")
        workforce = request.POST.get("workforce")
        requirement = request.POST.get("requirement")

        Requirement.objects.create(
            name=name,
            company=company,
            phone=phone,
            workforce=workforce,
            requirement=requirement
        )

    return render(request, "index.html")