from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from students.forms import VoteForm
from django.urls import reverse
from students.models import UserDetail
from django.shortcuts import render_to_response
from django.db import IntegrityError
from django.shortcuts import redirect



def home(request):
    return render(request, 'registration/login.html')
    

def loginf(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            print("disabled")
    else:
        print("invalid")
    
    return render(request, 'students/index.html')

class VoteView(FormView):
    template_name = "registration/vote.html"
    form_class = VoteForm

    def form_valid(self, form):
        try:
            form.save(self.request.user)    
            return super(VoteView, self).form_valid(form)
        except IntegrityError:
            return redirect("/error")
   
    def get_success_url(self, *args, **kwargs):
        return reverse("success")
