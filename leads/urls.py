from django.urls import path
from leads.views import (
    LeadDeleteView, LeadDetailView, LeadCreateView, 
    LeadListView, LeadUpdateView, AssignAgentView
)

app_name="leads"


urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'), #the first arg is the url path, the second arg is the function
    path('<int:pk>/', LeadDetailView.as_view(),name='lead-detail'),
    path('create/', LeadCreateView.as_view(),name='lead-create'),
    path('<int:pk>/update/', LeadUpdateView.as_view(),name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(),name='lead-delete'),   
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(),name='assign-agent'),
]
