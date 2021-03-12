from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path("login/", views.signin, name="Sign In"),
    path("logout/<int:id>/", views.signout, name = "Sign out"),
    path("", include(router.urls))
]
