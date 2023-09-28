import stripe
from rest_framework import status
from rest_framework.views import APIView
from django.conf import settings
from django.urls import reverse
from rest_framework.response import Response

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSession(APIView):
    def get(self, request):
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": "Advanced search",
                        },
                        "unit_amount": 1000,
                    },
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url=request.build_absolute_uri(reverse("success")),
            cancel_url=request.build_absolute_uri(reverse("cancel")),
        )
        return Response({"url": session.url}, status=status.HTTP_200_OK)


class SuccessView(APIView):
    def get(self, request):
        return {"success": True}


class CancelView(APIView):
    def get(self, request):
        return {"cancelled": True}
