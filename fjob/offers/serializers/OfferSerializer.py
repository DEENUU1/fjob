# from rest_framework import serializers
#
# from offers.models import offers
# from .SalariesSerializer import SalariesSerializer
#
#
# class OffersSerializer(serializers.ModelSerializer):
#     salary = SalariesSerializer(many=True, read_only=True)
#     is_new_offer = serializers.ReadOnlyField(source="is_new")
#
#     class Meta:
#         model = offers.Offers
#         fields = "__all__"
