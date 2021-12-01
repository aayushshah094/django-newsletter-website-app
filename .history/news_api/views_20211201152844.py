from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from .forms import CreateUserForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
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

class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        Userprofile = Profile.objects.get(pk=pk)
        user = Userprofile.user

        followers = Userprofile.followers.all()

        if len(followers) == 0:
            is_following = False

        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False

        number_of_followers = len(followers)

        context = {
            'user': user,
            'Userprofile': Userprofile,
            'is_following':is_following,
            'number_of_followers':number_of_followers,
        }

        return render(request, 'accounts/profile.html', context)
        
class ProfileEditView(UpdateView):
    model = Profile
    fields = ['name','email','profile_pic']
    template_name = 'accounts/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user

@login_required(login_url='login')

def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        posts_id = request.POST.get('posts_id')
        posts_obj = Post.objects.get(id=posts_id)
        profile = Profile.objects.get(user=user)

        if profile in posts_obj.liked.all():
            posts_obj.liked.remove(profile)
        else:
            posts_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, posts_id = posts_id)

        if not created:
            if like.value =='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        else:
            like.value = 'Like'

            posts_obj.save()
            like.save()

    return redirect(request.META.get('HTTP_REFERER'))

class UserSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        profile_list = Profile.objects.filter(
            Q(user__username__icontains=query,
            )
        )

        context = {
            'profile_list': profile_list, 
        }
        return render(request, 'accounts/search.html', context)

class AddFollower(View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.add(request.user)

        return redirect('profile', pk=profile.pk)

class RemoveFollower(View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.remove(request.user)

        return redirect('profile', pk=profile.pk)
