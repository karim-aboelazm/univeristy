from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import *
from random import randint
from django.db.models import Q

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('app:home') 
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

class HomePageView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_doctors"]= Doctors.objects.all().order_by('-id')
        return context
    

class DoctorsPageView(TemplateView):
    template_name = 'doctors.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_doctors"]= Doctors.objects.all().order_by('-id')
        return context
    
class StudentsPageView(TemplateView):
    template_name = 'student.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_students"]= Students.objects.all().order_by('-id')
        return context

class HallsPageView(TemplateView):
    template_name = 'halls.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_halls"]= Halls.objects.all().order_by('-id')
        return context

class SearchView(TemplateView):
    template_name = 'search.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get("search_keyword")
        context["search_student_result"]= Students.objects.filter(Q(code__icontains=kw)|
                                             Q(full_name__icontains=kw)|
                                             Q(group__icontains=kw)|
                                             Q(group_split__icontains=kw))
        
        context["search_doctor_result"]= Doctors.objects.filter(Q(code__icontains=kw)|
                                             Q(first_name__icontains=kw)|
                                             Q(last_name__icontains=kw)|
                                             Q(certify__icontains=kw)|
                                             Q(job_code__icontains=kw))
        
        context["search_halls_result"]= Halls.objects.filter(Q(code__icontains=kw)|
                                             Q(stage__icontains=kw)|
                                             Q(bulding__icontains=kw)|
                                             Q(spcial__icontains=kw))

        return context