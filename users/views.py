from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from users.models import Payment, User
from users.serializers import PaymentsSerializer, UserSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    serializer_class = PaymentsSerializer
    filterset_fields = (
        "course",
        "lesson",
        "payment_type",
    )
    ordering_fields = ("date_of_payment",)


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
