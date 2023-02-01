from django.urls import path
from .views import home, projects_datascience, projects_django, cursos, register_user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",home,name="home"),
    path("datascience_projects/", projects_datascience, name = "projects_datascience"),
    path("django_projects/", projects_django, name = "projects_django"),
    path("cursos/", cursos , name="cursos"),
    path("register/",register_user, name = "register"),
    
]
 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)