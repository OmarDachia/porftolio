from django import forms
from .models import Project
 
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'technologies', 'live_url', 'github_url']
        # You can also use exclude = ['field_to_exclude']
