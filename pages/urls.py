from django.urls import path
from pages.views import home_page_view
from .views import about_page_view
urlpatterns = [
    path("", home_page_view),
    path('about/', about_page_view),

]