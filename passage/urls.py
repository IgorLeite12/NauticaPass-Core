from rest_framework.routers import DefaultRouter
from .viewsets import PassageViewSet

router = DefaultRouter()
router.register(r'', PassageViewSet)

urlpatterns = router.urls