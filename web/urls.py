from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='amerixhome'),
    path('about-us/', views.about, name='amerixabout'),
    path('technology/', views.technology, name='amerixtechnology'),
    path('quality-programme', views.qualityprogramme, name='amerixqp'),
    path('careers', views.careers, name='amerixcareers'),
    path('leadership-team', views.leadershipteam, name='amerixleadership'),
    path('services', views.services, name='amerixservices'),
    path('port-services', views.portservices, name='amerixportservices'),
    path('warehousing', views.warehousing, name='amerixwarehousing'),
    path('transportation', views.transportation, name='amerixtransportation'),
    path('industries', views.industries, name='amerixindustries'),
    path('foodbeverage', views.foodbeverages, name='amerixfoodbev'),
    path('retail', views.retail, name='amerixretail'),
    path('consumergoods', views.consumergoods, name='amerixconsumergoods'),
    path('confectionnerylogistics', views.confectionnery, name='amerixconfectionnery'),
    path('blog', views.blog, name='amerixblog'),
    path('contact-us', views.contact, name='contact'),
    path('carriage', views.carriage, name='amerixcarriage'),
    path('ltl', views.ltl, name='amerixltl'),
    path('ceo', views.ceo, name='amerixceo'),
    path('transloading', views.transloading, name='amerixtransload'),
]