from django import forms

class RelatedForm(forms.Form):
    subject=forms.CharField(max_length=500)
    field=forms.BooleanField(required=False)

SUBJECT_RESOURCE_CHOICES=(
    ("MasterMind","MasterMind"),
    ("other","other"),
)
class TopicResourceForm(forms.Form):
    title=forms.CharField(max_length=500,widget=forms.TextInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'What this resource is ?',
                                }))
    description=forms.CharField(max_length=1500,required=False,widget=forms.Textarea(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'Description of what it is',
                                }))
    url=forms.URLField(widget=forms.TextInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'Proper Link of Resource',
                                    'help_text':'should be a link of type http:// or www.abc.com'
                                }))
class SubjectResourceForm(forms.Form):
    title=forms.CharField(max_length=500,widget=forms.TextInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'What this resource is ?',
                                }))
    description=forms.CharField(max_length=1500,required=False,widget=forms.Textarea(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'Description of what it is',
                                }))
    url=forms.URLField(widget=forms.TextInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'Proper Link of Resource',
                                    'help_text':'should be a link of type http:// or www.abc.com'
                                }))
    choice=forms.ChoiceField(choices=SUBJECT_RESOURCE_CHOICES,widget=forms.Select(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'Resource for topic'
                                }))