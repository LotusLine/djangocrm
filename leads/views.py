from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm
from django.views import generic

#Mixins are args that we pass in the inheritance of the classes


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

   

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class LeadListView(LoginRequiredMixin,generic.ListView):
    template_name = "lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = "lead_details.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = "lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        send_mail(
            subject="A lead has been created", 
            message="Got to admin to see new lead",
            from_email="test@test.com",
            recipient_list=["azadehbrownlee@gmail.com"]
        )

        return super(LeadCreateView, self).form_valid(form)
    

class LeadUpdateView(LoginRequiredMixin,generic.UpdateView):
    template_name = "lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name = "lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")
    









