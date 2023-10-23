import stripe
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import UserPackage, Package
from ..utils import generate_random_id
from ..permissions import IsPackageAlreadyOwned
from rest_framework.permissions import IsAuthenticated


UserModel = get_user_model()
stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSession(APIView):
    permission_classes = [IsAuthenticated, IsPackageAlreadyOwned]
    # authentication_classes = [SessionAuthentication]

    def get(self, request, package_id):
        user = request.user
        package = Package.objects.get(id=package_id)
        custom_id = generate_random_id.generate_random_id()

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": package.name,
                        },
                        "unit_amount": package.price,
                    },
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url=request.build_absolute_uri(
                reverse("success", kwargs={"custom_id": custom_id})
            ),
            cancel_url=request.build_absolute_uri(reverse("cancel")),
        )

        user_package = UserPackage.objects.filter(user=user, active=True).first()

        if user_package.package.id == 3:
            return Response(
                {"error": "You already have the best packages"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        elif user_package.package.id == 2 and package_id == 1:
            return Response(
                {"error": "You are not able to get worse packages"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user_package = UserPackage.objects.create(
            user=user,
            package=package,
            active=False,
            stripe_checkout_id=session.id,
            custom_id=custom_id,
        )
        user_package.save()

        return Response({"url": session.url}, status=status.HTTP_200_OK)
