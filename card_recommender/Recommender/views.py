from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import Http404
from .forms import ContactForm,PreferenceForm,ProfileForm
from django.views.generic.edit import FormView
import numpy as np
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import itertools
from sklearn.externals import joblib
from django.views.generic.edit import UpdateView,CreateView
from django.views.generic import DetailView
from .models import Card,Profile

def homepage(request):
    return render(request, 'home.html')


class ProfileView(UpdateView):
    form_class = ProfileForm
    template_name = "profile.html"
    success_url = '/'
    
    def get_object(self, queryset=None):

        # get the existing object or created a new one
        obj, created = Profile.objects.get_or_create(user=self.request.user)

        return obj
    
    def form_valid(self, form):
        name = form.cleaned_data['username']
        print(name)
        return super().form_valid(form)



class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
            
        
        
def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"contact",
        "content":"Welcome to the Contact page",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, "contact/view.html", context)
    
    
class ProductDetailView(DetailView):
    #queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
       context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
       print(context)
       return context


    def get_object(self, *args, **kwargs):
        request =self.request
        pk = self.kwargs.get('pk')
        instance = Card.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Card doesnt exist")
        return instance
