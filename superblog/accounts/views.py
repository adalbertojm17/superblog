from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView
from blog.models import Profile
from .forms import SingUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm


class CreateProfilePageView(CreateView):
    model= Profile
    form_class = ProfilePageForm
    template_name = 'registration/created_user_profile_page.html'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name ='registration/edit_profile_page.html'
    fields = ['bio','profile_pic','website_url']

class ShowProfilePageView(DetailView):
    model= Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        user = get_object_or_404(Profile,id= self.kwargs['pk'])
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        context['user'] = user
        return context

class UserRegisterView(generic.CreateView):
    form_class = SingUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    def get_object(self):
        return self.request.user
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')
def password_success(request):
    return render(request,'registration/password_success.html',{})
