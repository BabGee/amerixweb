from django.shortcuts import render

def index(request):
    return render(request, 'web/index.html')


def about(request):
    return render(request, 'web/about.html')


def technology(request):
    return render(request, 'web/technology.html')    


def qualityprogramme(request):
    return render(request, 'web/qualityprogramme.html')


def careers(request):
    return render(request, 'web/careers.html')


def leadershipteam(request):        
    return render(request, 'web/leadershipteam.html')


def services(request):
    return render(request, 'web/services.html')


def portservices(request):
    return render(request, 'web/portservices.html')


def warehousing(request):
    return render(request, 'web/warehousing.html')


def transportation(request):
    return render(request, 'web/transportation.html')


def industries(request):
    return render(request, 'web/industries.html')


def foodbeverages(request):
    return render(request, 'web/foodbev.html')


def retail(request):
    return render(request, 'web/retail.html')


def consumergoods(request):
    return render(request, 'web/consumergoods.html')


def confectionnery(request):
    return render(request, 'web/confectionnery.html')


def blog(request):
    return render(request, 'web/blog.html')


def contact(request):
    return render(request, 'web/contact.html')


def carriage(request):
    return render(request, 'web/carriage.html')


def ltl(request):
    return render(request, 'web/ltl.html')


def ceo(request):
    return render(request, 'web/ceo.html')


def transloading(request):
    return render(request, 'web/transloading.html')                                                        