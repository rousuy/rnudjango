from django.http import HttpResponse


# Create yours views here.
def home(request):
    return HttpResponse('Olá Django')
