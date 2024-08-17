from django.urls import path
from .views import CreateUserView


urlpatterns = [
    path('signup/', view=CreateUserView.as_view())
]
