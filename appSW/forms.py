from django import forms
from .models import  SequelsPros, Chapters

class chaptersForm(forms.ModelForm):
  class Meta:
    model = Chapters
    fields = "__all__"

class sequelsProsForm(forms.ModelForm):
  class Meta:
    model = SequelsPros
    fields = "__all__"