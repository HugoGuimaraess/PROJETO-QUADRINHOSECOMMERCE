from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from apps.usuarios.forms import LoginForms,CadastroForms
from django.core.mail import send_mail

#from django.contrib.sites.shortcuts import get_current_site
#from django.template.loader import render_to_string
#from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
#from django.utils.encoding import  force_bytes
#from django.contrib.auth.tokens import default_token_generator
#from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
# Create your views here.



def login(request):
    form=LoginForms()

    if request.method == 'POST':
        form=LoginForms(request.POST)

        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha_login'].value()


            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha

            )

            if usuario is not None:
                auth.login(request,usuario)
                messages.success(request,'Logado com sucesso')
                return redirect('index')
            else:
                messages.error(request,'erro ao logar, tente novamente')
                return redirect('login')


    return render(request,'usuarios/login.html',{'form':form})


@csrf_exempt
def cadastro(request):
    form=CadastroForms()

    if request.method == 'POST':
        form=CadastroForms(request.POST)
        if form.is_valid():
            nome=form['nome_cadastro'].value()
            emaill = form['email'].value()
            senha1=form['senha1'].value()



            if User.objects.filter(username=nome).exists():
                messages.error(request,'Usuário já existe')
                return redirect('cadastro')

            if User.objects.filter(email=emaill).exists():
                messages.error(request,'e-mail já existe')
                return redirect('cadastro')


            usuario = User.objects.create_user(
                username=nome,
                email=emaill,
                password=senha1,


            )

            current_site = get_current_site(request)
            mail_subject = 'Please activate Your Account'
            message = render_to_string('usuarios/ative.html',{
                'usuario':usuario,
                'domain':current_site,
                'uid' : urlsafe_base64_encode(force_bytes(usuario.pk)),
                'token': default_token_generator.make_token(usuario)
            })
            to_email= emaill
            send_email = EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()







            messages.success(request,'Thank you for using our website, we send you a verification e-mail so you can buy funkos. ')
            return redirect('login')


    return render(request,'usuarios/cadastro.html',{'form':form})



def logout(request):
    auth.logout(request)
    messages.success(request,'logout com sucesso')
    return redirect('index')


User = get_user_model()

def ative(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Usuário ativado com sucesso')
        return redirect('login')

    else:
        messages.error(request, 'Erro ao ativar usuário')
        return redirect('pagina_de_erro')










from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib import messages

User = get_user_model()

@csrf_exempt
def linkreset_email(request):
    form=CadastroForms()
    if request.method == 'POST':
        email = form['email'].value()
        if User.objects.filter(email=email):
            email = User.objects.get(email=email)
            current_site=get_current_site(request)
            mail_subject='pfv Reset sua senha'
            message= render_to_string('usuarios/resetpas.html',{
                'user':email,
                'uid':urlsafe_base64_encode(force_bytes(email.pk)),
                'domain':current_site,
                'token':default_token_generator.make_token(email)
            })
            to_email=email
            send_email=EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()
        else:
            messages.error(request,'erro')
            return redirect('linkreset_email')

    return render(request, 'usuarios/emailreset.html')





def dashboard(request):
    pass


