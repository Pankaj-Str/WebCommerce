from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100, help_text="100 caracteres máximo")
    email = forms.EmailField(required=True)
    comment = forms.CharField(widget=forms.Textarea, required=True)
