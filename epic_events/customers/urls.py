from rest_framework import routers

from .views import CustomerViewset

router.register(r'customers', CustomerViewset)
urlpatterns = router.urls