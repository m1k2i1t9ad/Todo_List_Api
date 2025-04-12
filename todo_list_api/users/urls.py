from django.urls import path
from .views import CustomTokenObtainPairView, RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),

]
