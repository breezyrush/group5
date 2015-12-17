from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': "usernameinput", 'class': "form-control", 'placeholder': "Username", 'required': "required"}),
                               max_length=200)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': "passwordinput", 'class': "form-control",
                                                                 'placeholder': "Password", 'required': "required"}), max_length=200)
