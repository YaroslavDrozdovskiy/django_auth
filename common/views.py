from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from common.forms import ProfileCreationForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount
# from common.models import UserProfile



class RegisterView(FormView):

    template_name='register.html',
    success_url=reverse_lazy('common:profile_create'),
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        login(self.request, authenticate(
            username=username, password=raw_password))
        return super().form_valid(form)


class CreateUserProfile(FormView):

    form_class = ProfileCreationForm
    template_name = 'profile_create.html'
    success_url = reverse_lazy('common:index')

    def dispatch(self, request, *args, **kwargs):
        """
        Если пользователь не зарегистрирован, то перенаправить на форму логина
        """
        if self.request.user.is_anonymous:
            return HttpResponseRedirect(reverse_lazy('common:login'))
        return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Заполняет форму информацией уже залогиненного пользователя
        """
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super(CreateUserProfile, self).form_valid(form)


def index(request):
    context = {}
    if request.user.is_authenticated:  
        context['username'] = request.user.username  
        # context['github_url'] = SocialAccount.objects.get(provider='github', user=request.user).extra_data['html_url']
    return render(request, 'index.html', context)


# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             auth.login(request, form.get_user())
#             return HttpResponseRedirect(reverse_lazy('common:index'))
#     else:
#         context = {'form': AuthenticationForm()}
#         return render(request, 'login.html', context)


# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse_lazy('common:index'))
