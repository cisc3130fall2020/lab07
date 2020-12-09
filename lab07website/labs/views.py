# /lab07/lab07website/labs/view.py

from django.shortcuts import render

#  Import the generic class based views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Import Lab model (python classes defined in the cwd aren't
# automatically available like they are in java and must be imported
# explicitly or implicitly.
from .models import *

# Create your views here.
class LabsListView(ListView):
    template_name = 'labs/list.html'
    model = Lab

    def get_queryset(self, **kwargs):
        """
        We need to make sure the list of labs is rendered to the
        html file so they can be displayed on the webpage. This
        is called rendering context data. ListView handles this
        with the get_queryset function.

        Simply specify that the queryset contains a reference to
        each lab in the database.
        """
        return Lab.objects.all()

class LabsDetailView(DetailView):
    # Tell Django the data for this webpage is a lab
    model = Lab
    
    # The webpage blueprint for the lab
    template_name = 'labs/detail.html'
