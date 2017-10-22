from django.conf.urls import url
from .views import carrentalView

urlpatterns =[

    url(r'^$',carrentalView.as_view(), name='home'),

]