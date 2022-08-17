from django.shortcuts import redirect, render
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User, UserManager
from .forms import LoginForm,UserRegistrationForm, ProfileEditForm, UserEditForm
from prediction_api.forms import PredictionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from prediction_api.models import Request, Result
from .model import predict_result
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required()
#if user has successfully been authenticated run this
def dashboard(request):
    result_created = None
    user = request.user
    if request.method == 'POST':
        pred_form = PredictionForm(request.POST)
        if pred_form.is_valid():
            cd = pred_form.cleaned_data
            title = cd['title']
            description = cd['description']
            created_request = Request.objects.create(request_owner=user, title=title, description=description)
            result = predict_result(description)
            print('Final result', result)
            result_created = Result.objects.create(request=created_request,result = result)
            print('Created result and request', result_created)
            return redirect('user:predictions')
    else:
            pred_form = PredictionForm()
    return render(request, 'account/dashboard.html', {'pred_form':pred_form})

@login_required()
def predictions(request):
    user = User.objects.get(username = request.user.username)
    user_status = user.is_superuser
    requests = Request.objects.filter(request_owner=user)
    results = None
    for a in requests:
        results = Result.objects.filter(request = a)
    all_requests = Request.objects.all()
    all_results = Result.objects.all()
    result_objects = Result.objects.all()
    latest_object = Result.objects.last()
    return render(request, 'account/prediction.html',
            {'result_objects':result_objects, 'latest_object':latest_object, 'requests':requests, 'results':results, 'user_status':user_status, 'all_results':all_results, 'all_requests':all_requests})

@login_required
def profile(request):
    username = request.user.username
    print(user)
    current_profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=current_profile)
        user_form = UserEditForm(request.POST, request.FILES, instance=request.user)

        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
    else:
        profile_form = ProfileEditForm(instance=current_profile)
        user_form = UserEditForm(instance=request.user)

    return render(request, 'account/profile.html', {'profile_form': profile_form, 'user_form':user_form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'account/password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users:dashboard')

def user_register(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      user = authenticate(request, username=cd['username'],password=cd['password'])

      if user is not None:
        login(request,user)
        return redirect('user:dashboard')
      else:
        messages.error(request, "Your Account Does Not Exist")

    else:
      messages.error(request,"Invalid Login")
  else:
    form = LoginForm()

  if request.method == 'POST':
    register_form = UserRegistrationForm(request.POST)
    if register_form.is_valid():
      new_user = register_form.save(commit=False)
      new_user.set_password(register_form.cleaned_data['password'])
      new_user.save()
      Profile.objects.create(user=new_user)
      login(request, new_user)
      messages.success(request,"Account Successfully Created")
      return redirect('user:dashboard')
  else:
    register_form=UserRegistrationForm()
  
  return render(request, 'account/register.html', {'form':form,'register_form':register_form})


def logout_request(request):
  logout(request)
  messages.info(request, "You Have Successfully Logged Out.")
  return redirect("user:register")





