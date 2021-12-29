from rest_framework import routers

from .views import EventViewset

router.register(r'events', EventViewset)
urlpatterns = router.urls