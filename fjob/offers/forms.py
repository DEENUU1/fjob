from django_filters import rest_framework as filters
from .models import Offers


class OffersFilter(filters.FilterSet):
    contract_type_name = filters.CharFilter(
        field_name="contract_type__name",
        lookup_expr="exact",
    )

    class Meta:
        model = Offers
        fields = {
            "experience_level__name": ["exact"],
            "salary__salary_from": ["gte", "lte"],
            "localizations__country": ["exact"],
            "localizations__city": ["exact"],
            "localizations__region": ["exact"],
            "title": ["icontains"],
            "is_remote": ["exact"],
            "is_hybrid": ["exact"],
            # 'contract_type_name': ['exact'],
        }
