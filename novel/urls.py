from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', views.NovelApiView, '')

urlpatterns = [
]
urlpatterns += router.urls