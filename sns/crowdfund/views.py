from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import CrowdFund


class CrowdFundCreateView(CreateView):
    model = CrowdFund


class CrowdFundDetailView(DetailView):
    model = CrowdFund


class CrowdFundListView(ListView):
    model = CrowdFund


class CrowdFundUpdateView(UpdateView):
    model = CrowdFund
