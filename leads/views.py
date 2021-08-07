from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm



#Django will provide the request to the function
def lead_list(request):
    #return HttpResponse("Hello Beautiful World")
    leads = Lead.objects.all()

    context = {
        "leads": leads  
    }

    return render(request, "lead_list.html",context) #first arg is the request, second arg is the name of template, third arg is a dict of values we wanna pass to the html


def lead_detail(request, pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    context = {
        "lead":lead
    }
    return render(request, "lead_details.html", context)


def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            return redirect("/leads")

    context = {
        "form":LeadForm()
    }
    return render(request,"lead_create.html", context)