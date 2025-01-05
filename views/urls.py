from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(prefix=r"books",viewset=views.BookViewSet, basename="book")
router.register(prefix=r"carts",viewset=views.CartViewSet,basename="cart")
router.register(prefix=r"items", viewset= views.CartItemViewSet, basename="demo") 
cart_item_router = routers.NestedDefaultRouter(router,"carts",lookup = 'cart')
cart_item_router.register("items",viewset= views.CartItemViewSet, basename='cart_item')
urlpatterns = [
    path('',include(router.urls)),
    path('',include(cart_item_router.urls)),
    path('collections/<int:id>',views.collection_list),

]