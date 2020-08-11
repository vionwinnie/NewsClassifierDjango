from django import forms

class NameForm(forms.Form):
    enter_text = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":13}))

