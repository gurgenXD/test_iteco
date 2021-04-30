from app.views import RollingStockViewSet, RollingStockProductsViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("rolling_stocks", RollingStockViewSet, basename="rolling_stocks")
router.register("rs_products", RollingStockProductsViewSet, basename="rs_products")
urlpatterns = router.urls
