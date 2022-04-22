from django.views.generic import TemplateView, ListView

from .models import Cheese


class HomePageView(ListView):
    model = Cheese
    paginate_by = 30
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
