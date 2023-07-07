from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .form import SignUpForm,EditProfileForm,EditUserForm
from django.contrib.auth import authenticate, login,logout
from .models import Profile
# Create your views here.



def login_view(request):
    context={}
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is None:
            context={"error":"Invalid username or password"}
            return render(request,"accounts/login.html",context)
        login(request,user)
        return redirect('/')
    return render(request,"accounts/login.html",context)



def signup_view(request):
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid : 
            form.save()
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            login(request,user)
            return redirect('accounts:profile')
    else:
        form=SignUpForm()
        return render(request,'accounts/signup.html',{'form':form})
    




@login_required
def logOut(request):
    logout(request)
    return redirect('/')


@login_required
def profile(request):
    profile=get_object_or_404(Profile,user=request.user)
    return render(request,'accounts/profile.html',{"profile":profile})

@login_required
def profile_edit(request):
    profile = get_object_or_404(Profile,user=request.user)
    if request.method == 'POST':
        formProfile = EditProfileForm(request.POST,request.FILES ,instance=profile)
        formUser=EditUserForm(request.POST,instance=profile.user)
        if formUser.is_valid() and formProfile.is_valid():
            formUser.save()
            myprofile = formProfile.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
            return redirect('accounts:profile')
    return render(request,"accounts/profile_edit.html",{"profile":profile})


    
    