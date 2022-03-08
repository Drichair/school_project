from django import forms
from django.contrib.auth.models import User
from main.models import UserIsVote

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']



class CreateVote(forms.Form):
    question = forms.CharField(
        label = 'Вопрос:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    ans1 = forms.CharField(
        label='Варианты ответа:',
        widget=forms.TextInput(
        attrs={
            'class': 'form-control'
             }
         )
    )
    ans2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )


class VoteY(forms.Form):
    question = forms.CharField(
        label='Вопрос:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    ans1 = forms.CharField(
        label='Варианты ответа:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    ans2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

class ToVote(forms.Form):
    class Meta:
        model = UserIsVote
        fields = ['choice']
        choices = ((1, 1), (2, 2),)
        widgets = {'choice': forms.RadioSelect(attrs={'name': 'vote'}, choices=choices)}



