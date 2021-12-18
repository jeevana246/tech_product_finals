from django.urls.conf import path
from compeapp import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="index"),
    path('ureg',views.ureg,name="ureg"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('adminregister',views.adminregister,name="adminregister"),
    path('scholarlogin',views.scholarlogin,name="scholarlogin"),
    path('scholarregister',views.scholarregister,name="scholarregister"),
    path('admin_dashboard',views.admin_dashboard,name="admin_dashboard"),
    path('hackathons',views.hackathons,name="hackathons"),
    path('competitions',views.competitions,name="competitions"),
    path('events',views.events,name="events"),
    path('adminlogout',views.adminlogout,name="adminlogout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)