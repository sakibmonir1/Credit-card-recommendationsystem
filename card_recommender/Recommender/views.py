from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import Http404
from .forms import ContactForm, PreferenceForm, ProfileForm
from django.views.generic.edit import FormView
import numpy as np
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import itertools
from sklearn.externals import joblib
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import DetailView
from .models import Card, Profile


def homepage(request):
    """
    This renders the HTML file
    """
    return render(request, 'home.html')


class ProfileView(UpdateView):
    """
    This class is used to show the profile

    ...

    Attributes
    ----------
    form_class : str
        a formatted string to print the ProfileForm
    template_name : str
        a HTML link which opens profile in a browser
    success_url : str
        a string which works when profile.html successfully runs
    """
    form_class = ProfileForm
    template_name = "profile.html"
    success_url = '/'

    def get_object(self, queryset=None):
        """
        get the existing object or created a new one
        """
        obj, created = Profile.objects.get_or_create(user=self.request.user)

        return obj

    def form_valid(self, form):
        """
        prints the taken input from the form


        Attributes
        ----------
        name : bytearray
            Takes input to keep data on a clean form


        """
        name = form.cleaned_data['username']
        print(name)
        return super().form_valid(form)


class SignUp(generic.CreateView):
    """
    This class is used for Sign Up
    ...

    Attributes
    ----------
    form_class : str
        a string that takes input from user creation form
    success_url : str
        unlock when user put the valid username and password
     template_name : str
        a HTML link which run when user successfully logged in

    """
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def contact_page(request):
    """
    if the contact form is valid contact page prints the cleaned data


    Parameters
    ----------
    contact_form : str
        This string takes given inputes
    """
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "contact",
        "content": "Welcome to the Contact page",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, "contact/view.html", context)


class ProductDetailView(DetailView):
    """"
    This class is used to view the detailed product


    Parameters
    ----------
    template_name : str
        This opens a HTML file to view detaled product

    """
    # queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        """
        This method gets the context data and prints accordingly


        Parameters
        ----------
        context : str
            This string takes the context data
        """

    context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
    print(context)
    return context


def get_object(self, *args, **kwargs):
    """
    This method works when it gets the valid instance. If the ID doesn't exist the card doesn't exist

    Parameters
    ----------
    request : str
        This string takes request

    pk : str
        This gets the self kwargs

    instance : str
        This string takes card the object from id
    """
    request = self.request
    pk = self.kwargs.get('pk')
    instance = Card.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Card doesnt exist")
    return instance
