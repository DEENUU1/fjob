import stripe
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.conf import settings
from django.urls import reverse
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import UserPackage, Package
from .serializers import PackageSerializer
from rest_framework.authentication import SessionAuthentication


UserModel = get_user_model()
stripe.api_key = settings.STRIPE_SECRET_KEY


class GetUserFreeUses(APIView):
    authentication_classes = [
        SessionAuthentication,
    ]

    def get(self, request):
        user = request.user
        package = Package.objects.get(id=1)
        user_package = UserPackage.objects.filter(user=user, active=True).first()
        if user_package.package == package:
            return Response(
                {"free_uses": user_package.package.free_users},
                status=status.HTTP_200_OK,
            )


class GetPackages(ListAPIView):
    serializer_class = PackageSerializer

    def get_queryset(self):
        queryset = Package.objects.all()
        return queryset


class CreateCheckoutSession(APIView):
    def get(self, request):
        user = request.user

        if UserPackage.objects.filter(user=user, active=True).exists():
            return Response(
                {"error": "You already have an active payment."},
                status=status.HTTP_403_FORBIDDEN,
            )

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": "Advanced search",
                        },
                        "unit_amount": settings.STRIPE_PRICE,
                    },
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url=request.build_absolute_uri(reverse("success")),
            cancel_url=request.build_absolute_uri(reverse("cancel")),
        )

        if Payment.objects.filter(user=user, active=False).exists():
            Payment.objects.filter(user=user, active=False).delete()

        payment = Payment.objects.create(
            user=user,
            stripe_checkout_id=session.id,
        )
        payment.save()

        return Response({"url": session.url}, status=status.HTTP_200_OK)


class SuccessView(APIView):
    def get(self, request):
        user = request.user
        payment = Payment.objects.get(user=user)
        payment.active = True
        payment.save()

        return Response({"success": True})


class CancelView(APIView):
    def get(self, request):
        return Response({"cancelled": True})
