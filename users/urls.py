from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import (
    PaymentViewSet,
    UserCreateApiView,
    UserListAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
    UserDestroyAPIView,
)

app_name = UsersConfig.name

router = SimpleRouter()
router.register("", PaymentViewSet)


class UserDeleteAPIView:
    pass


urlpatterns = [
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("register/", UserCreateApiView.as_view(), name="register"),
    path("", UserListAPIView.as_view(), name="users_list"),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="user_detail"),
    path("<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),
    path("<int:pk>/delete/", UserDestroyAPIView.as_view(), name="user_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
