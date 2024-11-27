from django import forms



class LoginForms(forms.Form):
    nome_login=forms.CharField(
        max_length=100,
        required=True,
        label='Login',
        widget=forms.TextInput(
            attrs={
                'placeholder':'EX: JOÃO',
                'class':'form-control'
            }
        )
    )
    senha_login=forms.CharField(
        max_length=100,
        label='Senha',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Digite sua Senha',
                'class':'form-control'
            }
        )
    )




class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder':'EX: João',
                'class':'form-control'
            }
        )
    )

    email = forms.EmailField(
        label='E-mail',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'placeholder':'EX = HUGO@AMBEV.COM.BR',
                'class':'form-control'
            }
        )
    )

    senha1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Digite sua senha',
                'class':'form-control'
            }
        )
    )
    senha2 = forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Digite sua senha',
                'class':'form-control'
            }
        )
    )





    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        nome = nome.strip()

        if ' ' in nome:
            raise forms.ValidationError('Espaços não são permitidos')
        else:
            return nome


    def clean_senha2(self):
        senha_1 = self.cleaned_data.get('senha1')
        senha_2 = self.cleaned_data.get('senha2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas devem ser iguais')
            else:
                return senha_2



