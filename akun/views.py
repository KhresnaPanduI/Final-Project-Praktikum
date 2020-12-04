from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.db.models.signals import post_save

from .forms import CreateUserForm, ProfileForm
from .models import Profile

# Create your views here.
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST, request.FILES)

			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('home')
			

		context = {
			'form': form
			}
		return render(request, 'akun/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'akun/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('home')

def home(request):
    return render(request, 'akun/index.html')

@login_required()
def set_apd(request):
	Profile.objects.get_or_create(user=request.user)
	profile = request.user.profile
	form = ProfileForm(instance=profile)

	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()

	context = {'form':form}
	return render(request, 'akun/input_data.html', context)


def list_apd(request):
	User = get_user_model()
	rs = User.objects.all()
	context = {
		'rs': rs
	}
	return render(request, 'akun/list-instansi.html', context)


def detail_apd(request, id):
    object = ProfileForm(data=model_to_dict(Profile.objects.get(id=id-1)))
    context = {
        'object': object
    }
    return render(request, 'akun/detail_apd.html', context)



