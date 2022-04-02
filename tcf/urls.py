from django.urls import path
from .import views

urlpatterns=[   
       path('index',views.index,name='index'),
       path('about',views.about,name='about'),
       path('contact',views.contact,name='contact'),
       path('faq',views.contact,name='faq'),
       path('partycake',views.partycake,name='partycake'),
       path('themecake',views.themecake,name='themecake'),
       path('tier',views.tier,name='tier'),
       path('cookies',views.cookies,name='cookies'),
       path('cupcakes',views.cupcakes,name='cupcakes'),
       path('minicake',views.minicake,name='minicake'),
       path('',views.register,name='register'),
       
]