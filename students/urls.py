from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from students import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home,name='home'),
    path('whoswinning',views.whoswining),
    path('login',auth_views.LoginView.as_view(),name='login'),
    path('accounts/login/',auth_views.LoginView.as_view(),name='loginAlt'),
    path('logout',auth_views.LogoutView.as_view(template_name='registration/login.html'),name='logout'),
    path('error',auth_views.LogoutView.as_view(template_name='registration/error.html'), name='error'),
    path('success',auth_views.LogoutView.as_view(template_name='registration/success.html'),name='success'),
    path('vote/', login_required(views.VoteView.as_view()), name="vote"),
]
