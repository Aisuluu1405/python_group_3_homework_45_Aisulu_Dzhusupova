from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES


class PlanForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Plan_name')
    text = forms.CharField(max_length=3000, required=False, label='Description', widget=widgets.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Status', initial=STATUS_CHOICES[0][0])
    deadline = forms.DateField(input_formats=['%Y-%m-%d'], required=False, label='Deadline')




