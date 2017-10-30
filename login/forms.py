from django.forms import Form, CharField
from django.forms.widgets import Input

class LoginForm(Form):
    user_email = CharField(label='Email', widget=Input(attrs={'Placeholder': 'Email', 'type': 'email', 'class': 'form-controls'}))
    user_password = CharField(label='Password', widget=Input(attrs={'Placeholder': 'Password', 'type': 'Password', 'class': 'form-controls'}))