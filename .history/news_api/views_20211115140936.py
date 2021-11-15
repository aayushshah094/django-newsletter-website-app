from django import urls
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm, Profileform
from django.contrib.auth.decorators import login_required
from .models import *
import requests
API_KEY= '6a48ce06539b47ae8812935869b85c61'

# Create your views here.
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
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')			
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return render(request,'accounts/logout.html')

@login_required(login_url='login')
def Profilepg(request):
    profile = request.user.profile
    form = Profileform(instance=profile)

    if request.method == 'POST':
        form = Profileform(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()
            
    context = {'form': form}
    return render(request, 'accounts/profile.html', context)

@login_required(login_url='login')
def home(request):
    all_articles = {}
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}' .format(keyword)
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        for i in articles:
            article_data = News(
                source = i['source'],
                author = i['author'],
                title = i['title'],
                description = i['description'],
                url = i['url'],
                urlToImage = i['urlToImage'],
                publishedAt = i['publishedAt'],
                content = i['content'],
            )
            article_data.save()
            all_articles = News.objects.all().order_by('-id')
    else:
        url = f'https://newsapi.org/v2/top-headlines?category=general&country=us&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

        for i in articles:
                article_data = News(
                    source = i['source'],
                    author = i['author'],
                    title = i['title'],
                    description = i['description'],
                    url = i['url'],
                    urlToImage = i['urlToImage'],
                    publishedAt = i['publishedAt'],
                    content = i['content'],
                )
                article_data.save()
                all_articles = News.objects.all().order_by('id')[:10]
        
    context = {
        'all_articles' : all_articles
    }
    return render(request, 'news_api/home.html', context)

@login_required(login_url='login')
def business(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}' .format(keyword)
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        for i in articles:
            article_data = News(
                source = i['source'],
                author = i['author'],
                title = i['title'],
                description = i['description'],
                url = i['url'],
                urlToImage = i['urlToImage'],
                publishedAt = i['publishedAt'],
                content = i['content'],
            )
            article_data.save()
            all_articles = News.objects.all().order_by('-id')
    else:
        url = f'https://newsapi.org/v2/top-headlines?category=business&country=us&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

        for i in articles:
                article_data = News(
                    source = i['source'],
                    author = i['author'],
                    title = i['title'],
                    description = i['description'],
                    url = i['url'],
                    urlToImage = i['urlToImage'],
                    publishedAt = i['publishedAt'],
                    content = i['content'],
                )
                article_data.save()
                all_articles = News.objects.all().order_by('-id')[:10]
        
    context = {
        'all_articles' : all_articles
    }

    return render(request, 'news_api/business.html', context)

@login_required(login_url='login')
def technology(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}' .format(keyword)
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        for i in articles:
            article_data = News(
                source = i['source'],
                author = i['author'],
                title = i['title'],
                description = i['description'],
                url = i['url'],
                urlToImage = i['urlToImage'],
                publishedAt = i['publishedAt'],
                content = i['content'],
            )
            article_data.save()
            all_articles = News.objects.all().order_by('-id')
    else:
        url = f'https://newsapi.org/v2/top-headlines?category=technology&country=us&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

        for i in articles:
                article_data = News(
                    source = i['source'],
                    author = i['author'],
                    title = i['title'],
                    description = i['description'],
                    url = i['url'],
                    urlToImage = i['urlToImage'],
                    publishedAt = i['publishedAt'],
                    content = i['content'],
                )
                article_data.save()
                all_articles = News.objects.all().order_by('-id')[:10]
        
    context = {
        'all_articles' : all_articles
    }

    return render(request, 'news_api/technology.html', context)

@login_required(login_url='login')
def general(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}' .format(keyword)
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        for i in articles:
            article_data = News(
                source = i['source'],
                author = i['author'],
                title = i['title'],
                description = i['description'],
                url = i['url'],
                urlToImage = i['urlToImage'],
                publishedAt = i['publishedAt'],
                content = i['content'],
            )
            article_data.save()
            all_articles = News.objects.all().order_by('-id')
    else:
        url = f'https://newsapi.org/v2/top-headlines?category=general&country=us&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

        for i in articles:
                article_data = News(
                    source = i['source'],
                    author = i['author'],
                    title = i['title'],
                    description = i['description'],
                    url = i['url'],
                    urlToImage = i['urlToImage'],
                    publishedAt = i['publishedAt'],
                    content = i['content'],
                )
                article_data.save()
                all_articles = News.objects.all().order_by('-id')[:10]
        
    context = {
        'all_articles' : all_articles
    }
    return render(request, 'news_api/general.html', context)

@login_required(login_url='login')
def health(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}' .format(keyword)
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        for i in articles:
            article_data = News(
                source = i['source'],
                author = i['author'],
                title = i['title'],
                description = i['description'],
                url = i['url'],
                urlToImage = i['urlToImage'],
                publishedAt = i['publishedAt'],
                content = i['content'],
            )
            article_data.save()
            all_articles = News.objects.all().order_by('-id')
    else:
        url = f'https://newsapi.org/v2/top-headlines?category=health&country=us&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

        for i in articles:
                article_data = News(
                    source = i['source'],
                    author = i['author'],
                    title = i['title'],
                    description = i['description'],
                    url = i['url'],
                    urlToImage = i['urlToImage'],
                    publishedAt = i['publishedAt'],
                    content = i['content'],
                )
                article_data.save()
                all_articles = News.objects.all().order_by('-id')[:10]
        
    context = {
        'all_articles' : all_articles
    }
    return render(request, 'news_api/health.html', context)

@login_required(login_url='login')
def sports(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}' .format(keyword)
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        for i in articles:
            article_data = News(
                source = i['source'],
                author = i['author'],
                title = i['title'],
                description = i['description'],
                url = i['url'],
                urlToImage = i['urlToImage'],
                publishedAt = i['publishedAt'],
                content = i['content'],
            )
            article_data.save()
            all_articles = News.objects.all().order_by('-id')
    else:
        url = f'https://newsapi.org/v2/top-headlines?category=sports&country=us&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

        for i in articles:
                article_data = News(
                    source = i['source'],
                    author = i['author'],
                    title = i['title'],
                    description = i['description'],
                    url = i['url'],
                    urlToImage = i['urlToImage'],
                    publishedAt = i['publishedAt'],
                    content = i['content'],
                )
                article_data.save()
                all_articles = News.objects.all().order_by('-id')[:10]
        
    context = {
        'all_articles' : all_articles
    }
    return render(request, 'news_api/sports.html', context)

@login_required(login_url='login')
def entertainment(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}' .format(keyword)
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        for i in articles:
            article_data = News(
                source = i['source'],
                author = i['author'],
                title = i['title'],
                description = i['description'],
                url = i['url'],
                urlToImage = i['urlToImage'],
                publishedAt = i['publishedAt'],
                content = i['content'],
            )
            article_data.save()
            all_articles = News.objects.all().order_by('-id')
    else:
        url = f'https://newsapi.org/v2/top-headlines?category=entertainment&country=us&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

        for i in articles:
                article_data = News(
                    source = i['source'],
                    author = i['author'],
                    title = i['title'],
                    description = i['description'],
                    url = i['url'],
                    urlToImage = i['urlToImage'],
                    publishedAt = i['publishedAt'],
                    content = i['content'],
                )
                article_data.save()
                all_articles = News.objects.all().order_by('-id')[:10]
        
    context = {
        'all_articles' : all_articles
    }
    return render(request, 'news_api/entertainment.html', context)

@login_required(login_url='login')
def science(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}' .format(keyword)
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        for i in articles:
            article_data = News(
                source = i['source'],
                author = i['author'],
                title = i['title'],
                description = i['description'],
                url = i['url'],
                urlToImage = i['urlToImage'],
                publishedAt = i['publishedAt'],
                content = i['content'],
            )
            article_data.save()
            all_articles = News.objects.all().order_by('-id')
    else:
        url = f'https://newsapi.org/v2/top-headlines?category=science&country=us&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

        for i in articles:
                article_data = News(
                    source = i['source'],
                    author = i['author'],
                    title = i['title'],
                    description = i['description'],
                    url = i['url'],
                    urlToImage = i['urlToImage'],
                    publishedAt = i['publishedAt'],
                    content = i['content'],
                )
                article_data.save()
                all_articles = News.objects.all().order_by('-id')[:10]
        
    context = {
        'all_articles' : all_articles
    }
    return render(request, 'news_api/science.html', context)

def businessDB(request):
    business_list = News.objects.all()
    return render (request, 'business.html', {'business_list':business_list} )

def homeDB(request):
    home_list = News.objects.all()
    return render (request, 'home.html', {'home_list':home_list} )

def generalDB(request):
    general_list = News.objects.all()
    return render (request, 'general.html', {'business_list':general_list} )

def healthDB(request):
    health_list = News.objects.all()
    return render (request, 'health.html', {'health_list':health_list} )

def sportsDB(request):
    sports_list = News.objects.all()
    return render (request, 'sports.html', {'sports_list':sports_list} )

def entertainment(request):
   entertainment_list = News.objects.all()
    return render (request, 'entertainment.html', {'home_list':home_list} )