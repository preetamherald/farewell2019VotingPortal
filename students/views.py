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
from collections import Counter


def whoswining(request):

    mr_vsit = UserDetail.objects.all().values_list('Mr_VSIT', flat=True) 
    ms_vsit = UserDetail.objects.all().values_list('Ms_VSIT', flat=True) 
    mr_vsit_winner = []
    ms_vsit_winner = []

    for x in mr_vsit:
        f_name = (User.objects.all().filter(pk=x).values_list('first_name', flat=True))[0]
        l_name = (User.objects.all().filter(pk=x).values_list('last_name', flat=True))[0]
        name = f_name + " " + l_name
        mr_vsit_winner.append(name)

    for x in ms_vsit:
        f_name = (User.objects.all().filter(pk=x).values_list('first_name', flat=True))[0]
        l_name = (User.objects.all().filter(pk=x).values_list('last_name', flat=True))[0]
        name = f_name + " " + l_name
        ms_vsit_winner.append(name)

    winner_m =Counter(mr_vsit_winner)
    winner_f =Counter(ms_vsit_winner)

    context = {
        "Mr_VSIT": winner_m.most_common(3),
        "Ms_VSIT": winner_f.most_common(3),
    }

    return render(request, 'registration/result.html', context)

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
