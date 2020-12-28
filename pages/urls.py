from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.index, {'pagename': ''}, name='index'),
    path('contact', views.contact, name='contact'),
    path('testpage', TemplateView.as_view(template_name='pages/page.html')),
    path('<str:pagename>', views.index, name='index'),

]