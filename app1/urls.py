from django.urls import path
from app1 import views




urlpatterns= [
    path("",views.interface,name="interface"),
    path("user",views.userlogin,name="userlogin"),
    path("Login",views.adminlogin,name="adminlogin"),
    path("<int:id>/view",views.cltview,name='cltview'),
    path("<int:id>/update",views.cltupdate,name='cltupdate'),
    path("<int:id>/delete",views.cltdelete,name='cltdelete'),
    path("addclt",views.addclt,name='addclt'),
    path("<int:id>/project",views.proj_detail,name='project_details'),

]