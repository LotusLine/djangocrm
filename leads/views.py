from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm
from django.views import generic



class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class LeadListView(generic.ListView):
    template_name = "lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(generic.DetailView):
    template_name = "lead_details.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(generic.CreateView):
    template_name = "lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")
    

class LeadUpdateView(generic.UpdateView):
    template_name = "lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadDeleteView(generic.DeleteView):
    template_name = "lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")
    









