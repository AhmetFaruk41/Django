from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('kurslar/', include('courses.urls')),
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]


#courseapp
#courses
#pages
