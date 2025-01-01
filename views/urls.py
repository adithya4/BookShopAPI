from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(prefix=r"books",viewset=views.BookViewSet, basename="book")
urlpatterns = [
    path('',include(router.urls)),
    path('collections/<int:id>',views.collection_list)
]