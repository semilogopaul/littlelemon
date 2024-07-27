from django.urls import path
from .views import MenuItemView, SingleMenuItemView, index

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]
