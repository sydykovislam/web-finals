from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.products.views import *
from apps.categories.views import category_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main-page'),
    path('<int:pk>/', product_detail, name='product-detail'),
    path('category/<int:pk>/', category_detail, name='category'),
    path('cart/', include('apps.cart.urls')),
    path('user/', include('apps.users.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
