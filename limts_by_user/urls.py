from django.urls import path

from .views import UserLimitsListView

urlpatterns = [
    path('user_limits/', UserLimitsListView.as_view(), name='user_limits'),

]
