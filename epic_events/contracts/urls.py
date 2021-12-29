from rest_framework import routers

from .views import ContractViewset

router.register(r'contracts', ContractViewset)
urlpatterns = router.urls