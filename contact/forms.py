from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100, help_text="100 caracteres máximo")
    email = forms.EmailField(required=True)
    comment = forms.CharField(widget=forms.Textarea, required=True)
