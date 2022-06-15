from django.urls import path
# from . import views
from .views import DashboardView, Detail
urlpatterns = [
    
    # path('', views.dashboard, name="dashboard"),
    path('', DashboardView.as_view(), name="dashboard"),
    path('detail/<int:pk>', Detail.as_view(), name='detail')
]
