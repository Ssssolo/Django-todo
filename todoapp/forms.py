from django import forms
from .models import Todo
from allauth.account.forms import LoginForm, SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

class AdaugareForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Salveaza', css_class='btn-success'))
    
    class Meta:
        model = Todo
        fields = ('titlu', 'descriere')

class EditareForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Salveaza', css_class='btn-success'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_creare'].disabled = True

    class Meta:
        model = Todo
        fields = ("__all__")

# Modificam aspectul formularului de login
class NewLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modificam numele labelului
        self.fields['password'].label = "Parola"

        # Adaugam o clasa si placeholder
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Introduceti numele'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Introduceti parola'})


class NewRegisterForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Introduceti numele'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Introduceti adresa de email'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Introduceti parola'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Repetati parola'})