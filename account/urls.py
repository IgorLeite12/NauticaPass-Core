from rest_framework.routers import DefaultRouter
from .viewsets import AccountViewSet

router = DefaultRouter()
router.register(r'', AccountViewSet)

urlpatterns = router.urls