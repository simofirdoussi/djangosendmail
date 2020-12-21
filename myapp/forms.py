from django import forms

class Sendit(forms.Form):
    name = forms.CharField()
    subject = forms.CharField()
    email = forms.EmailField() 
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(Sendit, self).__init__(*args, **kwargs)