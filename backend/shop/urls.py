from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

from accounts.views import signup, logout_user, login_user

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<str:sluglink>/', views.product_details, name='product_detail'),
    path('cart/', views.cart, name='cart'),
path('cart/delete/', views.delete_cart, name='delete_cart'),
    path('product/<str:sluglink>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)