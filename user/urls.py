from rest_framework.routers import DefaultRouter
from .views import ProfileView
from rest_framework.routers import DefaultRouter

from .views import ProfileView

router_v1 = DefaultRouter()
router_v1.register('profiles', ProfileView)
