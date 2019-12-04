from django import forms
from django.contrib.auth import get_user_model


class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Sua Senha",
            }
        )
    )


user = get_user_model()


class registerForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Seu email",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Sua senha",
            }
        )

    )
    passwordConfirmation = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirme a senha \n",
    )

    # validacaoes de registro
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = user.objects.filter(username=username)
        if qs.exists():
            raise (forms.ValidationError("Username usado"))

        return (username)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = user.objects.filter(email=email)
        if qs.exists():
            raise (forms.ValidationError("Email usado"))

        return (email)

    def clean(self):
        data = self.cleaned_data
        password = data.get("password")
        passwordConfirmation = data.get("passwordConfirmation")
        if (password != passwordConfirmation):
            raise (forms.ValidationError("Senhas diferentes!"))
        else:
            return data
