from django.contrib import admin
from django.urls import path, include  # import include
from crudApp import views

urlpatterns = [
    path('admin/', admin.site.urls),


    # Set the root URL to the medicine card view
    path('', include('Medicine_inventory.urls')),  # now root goes to medicine app

]