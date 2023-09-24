from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (RecipeViewSet, ShopViewSet, FavoriteViewSet,
                    FollowViewSet, IngredientViewSet, TagViewSet)

router = SimpleRouter()


router.register('tags', TagViewSet, basename='tags')
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('recipes/download_shopping_cart', ShopViewSet, basename='shop')
router.register(r'recipes/(?P<id>\d+)/favorite', FavoriteViewSet, basename='favorite')
router.register('users/subscriptions', FollowViewSet, basename='subscribe')
router.register('ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

]
