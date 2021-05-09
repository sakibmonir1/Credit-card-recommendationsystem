from django.shortcuts import render
from django.views.generic import ListView

from recommender.models import Card


class SearchProductView(ListView):
    """
    A class to represent the product view's search


    ...


    Attributes
    ----------
    template_name : str
        a string to show the HTML link
    """
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        """
        This method used to get the context data

        ...


        Parameters
        ----------

        get_context_data : str
            a formatted string is used to get the context
        request.GET.get : query
            a string to get the query

        """
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        """
        This method prints card objects if query is done and prints card object search if the query is not done


        Parameters
        ----------

        request : request
            get the request from self request

        Attributes
        ----------

        method_dict : request
            get the request and keep in method_dict

        query : get the dict method and keep into query

        """
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            print(Card.objects.search(query))
            return Card.objects.search(query)
        return Card.objects.features()

