from django.urls import path, include
from .views import EmployeeViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register(r'employees', EmployeeViewSet)
router.register(r'employees', EmployeeViewSet)

# urlpatterns = router.urls
urlpatterns = [
    path('api/', include(router.urls)),
]