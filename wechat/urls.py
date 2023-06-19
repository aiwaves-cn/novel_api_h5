from . import views
from rest_framework.routers import SimpleRouter
from django.urls import path, include

router = SimpleRouter()
router.register('', views.WechatView, '')
urlpatterns = [

]
urlpatterns += router.urls
