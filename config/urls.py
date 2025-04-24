# from django.contrib import admin
# from django.urls import path, include
#
# from django.urls import re_path
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
#
# from user_auth.view.logout_view.LogoutView import *
#
# schema_view = get_schema_view(
#    openapi.Info(
#       title="Snippets API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny,],
# )
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include('user_auth.urls')),
#     path('api/logout/', LogoutView.as_view(), name='logout'),
#
#     re_path(r'^swagger(?P<format>\.json|\.yaml)/$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from user_auth.view.logout_view.LogoutView import *

# Настройка Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include([
        path('logout/', LogoutView.as_view(), name='logout'),


        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),


        re_path(r'^swagger(?P<format>\.json|\.yaml)/$', schema_view.without_ui(cache_timeout=0), name='swagger-json'),


        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
    ])),
]
