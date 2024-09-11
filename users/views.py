from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from users.models import Payment
from users.serializers import PaymentsSerializer


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

