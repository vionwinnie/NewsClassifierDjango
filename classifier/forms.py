from django import forms

class NameForm(forms.Form):
    enter_text = forms.CharField(widget=forms.Textarea(attrs={"rows":20, "cols":50}))
    #your_name = forms.CharField(label='Your name', max_length=100)
