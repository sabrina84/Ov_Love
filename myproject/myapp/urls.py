from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^home/',  views.start, name='home'),
    url(r'^signup/', views.home, name='signup'),

    url(r'^login/', views.home2, name='login'),
    url(r'^signedup/', views.signup, name='signedup'),
    url(r'^loggedin/', views.login, name='loggedin'),
    url(r'^home_/', views.home_, name='home_'),
    url(r'^home2/', views.home3, name='home2'),
    url(r'^profile/', views.profile, name='profile'),

    url(r'^gotit/', views.gotit, name='gotit'),
    url(r'^loggedout/', views.logout, name='loggedout'),
    url(r'^faq/', views.faq, name='faq'),
    url(r'^symptom/', views.symptom, name='symptom'),
    url(r'^result/', views.result, name='result'),
    url(r'^control/', views.control, name='control'),
    url(r'^question/', views.question, name='question'),
    url(r'^profile_/', views.profile_, name='profile_'),
    url(r'^calorie/', views.calorie, name='calorie'),
    url(r'^workout/', views.workout, name='workout'),



]
