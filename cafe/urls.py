from django.urls import path
from . import views

app_name = 'cafe'
urlpatterns = [
    path('', views.index, name='index'),  # 메인 페이지
    path('menu/', views.menu, name='menu'),  # 메뉴 페이지
    path('menu/<int:menu_id>', views.menu_detail, name='menu_detail'),
    path('event/', views.event, name='event'),  # 이벤트 페이지
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('store/', views.store, name='store'),  # 매장 소개 페이지
]
