from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import NewUserForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import forms, AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse
from django.core.mail import send_mail,EmailMessage
from Loginproject.settings  import EMAIL_HOST_USER


# Create your views here.

@login_required
def Homepage(request):
    print(request.COOKIES.items())
    return render(request, "Home.html")


# def login_user(request):
#     if request.method == "POST":
#         print(request.POST)
#         form = AuthenticationForm(request,data=request.POST)
#         if form.is_valid():
#             username = form.changed_data.get('username')
#             password = form.changed_data.get('password')
#             user=authenticate(username=username,password=password)
#
#             if user is not None:
#                 login(request,user)
#                 messages.info(request, f"You are now logged in as {username}.")
#
#         return redirect("Home")
#
#     else:
#         #messages.error(request,"credential not correct!!please try again!!")
# return render(request, "Login.html",{"login_form":AuthenticationForm()})




def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )

            #mail send
            subject = 'Welcome to Pythonworld'
            message = f'your login credential is username is {request.POST["username"]} '
            email = request.POST["email"]
            #file = r"C:\Users\pratidan\Desktop\git.txt"

            print((email))

            # send_mail(subject,message, EMAIL_HOST_USER, [email], fail_silently=False)  #To send mail without attchment
            try:
                mail = EmailMessage(subject, message,EMAIL_HOST_USER, [email])
    #           mail.attach_file(r"C:\Users\pratidan\PycharmProjects\Loginproject\app1\tests.py")
                mail.send(fail_silently=False)
                print("Mail send successfully .....")
            except Exception as e:
                print("we have issue in mail sending!!! please check...",e)


            return redirect("Login")

        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="Register.html", context={"register_form":form})


def login_user(request):
    print(request.method)
    if request.method == "POST":
        print(request.POST)
        form = AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user :

                login(request, user)

                messages.success(request, f"You are now logged in as {username}")
                return redirect("Home")
            else:
                messages.error(request, "Invalid username or password of user")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request=request, template_name="Login.html", context={"login_form":form})



def logut_user(request):
    logout(request)
    messages.success(request,"Logout successfully!!")
    return redirect("Login")


# class SignUpView(SuccessMessageMixin,CreateView):
#
#     form_class = SignUpForm
#     success_message = "The user is added succefully!!"
#     success_url = reverse_lazy('Login')
#
#     template_name = 'Register.html'


def setcookies(request):
    response = render(request,'cookies.html')
    response.set_cookie(key='name',value="Pratik")
    response.set_cookie(key='age',value=20)
    return response

def getcookies(request):
    nm = request.COOKIES.get("name")
    ag = request.COOKIES.get("age")
    return render(request,"show_cookies.html")

def deletecookies(request):
    response = redirect("Home")
    response.delete_cookie('name')
    response.delete_cookie('age')
    return response


def cookies_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>Test cookies<h1>")

def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("cookies created")
    else:
        response = HttpResponse("<h1> Your browser doesnot accept cookies<h1>")
    return response



def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>The session is set</h1>")



def access_session(request):
    response = "<h1>Welcome to Sessions </h1><br>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('createsession')


def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("<h1>dataflair<br>Session Data cleared</h1>")



def middlewearException(request):
    result = 5/0
    print(result)










