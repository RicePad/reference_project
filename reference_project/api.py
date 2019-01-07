from rest_framework import routers
from jobs import api_views as myapp_views

router = routers.DefaultRouter()
router.register(r'jobs', myapp_views.JobViewSet)
