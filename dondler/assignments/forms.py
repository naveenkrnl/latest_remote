from django import forms
from .models import SubmitAssignment,Assignment

class SubmitForm(forms.Form):
    description = forms.CharField(label='Description', required=False, widget=forms.Textarea(attrs=
                            {
                                'class':'form-control',
                                'placeholder' : 'Describe your submission (If required)',
                            }))
    link = forms.URLField(label='Link',required=False, widget=forms.TextInput(attrs=
                            {
                                'class':'form-control',
                                'placeholder' : 'Link to your Assignment (If required)',
                            }))
    files = forms.FileField(label='File',required=False)
        

class CreateAssignmentForm(forms.ModelForm):      

    class Meta:
        model=Assignment
        exclude=[
            "user",
            "semester"
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['last_date'].widget=forms.DateTimeInput()
        for field in iter(self.fields):
            if self.fields[field].widget.__class__.__name__ in ('AdminTextInputWidget' , 'Textarea' ,'TextInput','URLInput', 'NumberInput' , 'AdminURLFieldWidget', 'Select'): 
                self.fields[field].widget.attrs.update({ 'class': 'form-control' })