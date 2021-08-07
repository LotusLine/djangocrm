from django import forms


#class LeadModelForm(forms.ModelForm):
    #class Meta:



class LeadForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    age = forms.IntegerField(min_value=0)
 