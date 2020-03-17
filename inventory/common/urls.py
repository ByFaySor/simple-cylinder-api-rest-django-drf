from django.urls import include, path
from rest_framework.routers import DefaultRouter
from inventory.common import views

# Create a router and register our viewsets with it.
router = DefaultRouter(trailing_slash=False)
router.register('type-cyliders', views.TpsCylinderViewSet)
router.register('cyliders', views.DtsCylinderViewSet)
router.register('persons', views.DtsPersonViewSet)
router.register('cylider-persons', views.DtsCylinderPersonViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]