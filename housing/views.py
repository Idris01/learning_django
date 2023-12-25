from django.shortcuts import render
from django.http import HttpResponse
from .models import House

# Create your views here.
def home_view(request):
    print(request)
    houses = House.objects.all()

    return render(
            template_name="home.html",
            request=request,
            context={"houses":houses}
            )
