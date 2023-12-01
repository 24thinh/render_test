from django import forms

from .models import Work, Description, Entry

class WorkForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['due_date'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd ',
                'class': 'form-control'
                }
            )

    class Meta:
        model = Work
        fields = ['text', 'due_date']
        labels = {'text': 'Title', 'due_date': 'Due date' }

class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Description
        fields = ['describe', 'resource']
        labels = {'describe': 'Describe', 'resource': 'Resource'}
        """widgets = {
            'due_date': forms.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            )
        }"""

class EntryForm(forms.ModelForm):
   # image = forms.ImageField(
   #     label = "Image",
   #     widget=forms.ClearableFileInput(attrs={"multiple": True}),
   # )

    class Meta:
        model = Entry
        fields = ['text', 'image']
        labels = {'text': 'Text', 'image': 'Image'}