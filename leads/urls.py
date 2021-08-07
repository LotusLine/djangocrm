from django.urls import path
from leads.views import lead_detail, lead_list , lead_create

app_name="leads"

urlpatterns = [
    path('', lead_list), #the first arg is the url path, the second arg is the function
    path('create/', lead_create),
    path('<int:pk>/', lead_detail),
    
    
]
