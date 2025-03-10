from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from myap import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index,name="index"),
    path('', views.home,name="home"),
    path('travel/<int:id>/', views.detail,name="detail"),
    path('add_new/', views.add_new,name="add_new"),
    path('update/<int:id>/', views.update,name="update"),
    path('delete/<int:id>/', views.delete,name="delete"),
    path('plan/', views.plan,name="plan"),
    path('info/', views.info,name="info"),
    path('map/', views.map,name="map"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
