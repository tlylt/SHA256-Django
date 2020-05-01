from django import forms

# forms.Form with a caplital F, not form


class HashForm(forms.Form):
    text = forms.CharField(label="", widget=forms.Textarea(
        attrs={'placeholder': 'Type whatever you want to be encrypted here'}))
