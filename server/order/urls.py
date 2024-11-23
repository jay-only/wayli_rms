# home/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('menu/', views.menu_view, name='menu'),

    # path('create-order/', views.create_order, name='create_order'),
    path('order-list/', views.order_list, name='order_list'),
    path('kitchen/', views.kitchen_view, name='kitchen_view'),
    path('order/mark_prepared/<int:order_id>/', views.mark_prepared, name='mark_prepared'),

    # path('update-order-status/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('order/<int:order_id>/complete/', views.mark_order_complete, name='mark_order_complete'),
    path('order/<int:order_id>/paid/', views.mark_order_paid, name='mark_order_paid'),
    path('review/', views.order_review, name='order_review'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
