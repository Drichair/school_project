from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        label="Ваш логин",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        max_length=20,
        label= "Ваш пароль",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
