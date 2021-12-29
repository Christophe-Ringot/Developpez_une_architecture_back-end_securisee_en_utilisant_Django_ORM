from rest_framework import routers

from .views import UserViewSet

router.register(r'user', UserViewSet)
urlpatterns = router.urls