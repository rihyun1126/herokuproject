from django.contrib import admin
from django.urls import path, include
import board.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board.views.show, name = 'show'),
    path('', board.views.home, name = 'home'),
    path('board/', include('board.urls')),
    path('about/', board.views.about, name = 'about'),
    path('result/', board.views.result, name = 'result'),
]