from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from AppTwo.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# from AppTwo.models import UserForm, UserProfileInfo
# from . import forms
# from AppTwo.forms import NewUserForm
# Create your views here.
# def index(request):
#     return HttpResponse("<em>My Second App</em>")
# def help(request):
#         my_dict = {'insert_me':" I am from views.py !"}
#         return render(request,'AppTwo/help.html',context = my_dict)
def index(request):
        # context_dict = {'text': 'hello world', 'number':100}
        # return render(request,'AppTwo/index.html', context_dict)
        return render(request, 'AppTwo/index.html')

def special(request):
    return HttpResponse("Logged in!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'AppTwo/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'AppTwo/login.html',{})
# def other(request):
#         return render(request,'AppTwo/other.html')
#
# def relative(request):
#         return render(request,'AppTwo/relative_url_templates.html')

# def users(request):
#     form = NewUserForm()
#
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#
#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print('Form Invalid')
#
#     return render(request, 'AppTwo/users.html', {'form' : form})

# def users(request):
#         user_list = User.objects.order_by('first_name')
#         user_dict = {'users':user_list}
#         return render(request,'AppTwo/users.html',context = user_dict)
#
# def form_name_view(request):
#     form = forms.FormName()
#
#     if request.method ==  'POST':
#         form = forms.FormName(request.POST)
#
#         if form.is_valid():
#             print("VALIDATION SUCCESS!")
#             print("NAME "+form.cleaned_data['name'])
#             print("EMAIL "+form.cleaned_data['email'])
#             print("TEXT "+form.cleaned_data['text'])
#     return render(request, 'AppTwo/form_page.html', {'form':form})
