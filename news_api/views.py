from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
import requests
API_KEY= '6a48ce06539b47ae8812935869b85c61'

# Create your views here.

@login_required(login_url='login')
def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']



    context = {
        'articles' : articles
    }

    return render(request, 'news_api/home.html', context)

def registerPage(request):
	if request.user.is_authenticated:
		return render(request, 'news_api/home.html')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

	context = {'form':form}
	return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return render(request,'news_api/home.html')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return render(request,'news_api/home.html')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return render(request,'accounts/logout.html')
