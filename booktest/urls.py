from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$',views.index),
    url(r'^books$',views.show_books),
    url(r'^books/(\d+)$',views.detail)
]