from django import forms


class OfferFilterForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)
    country = forms.CharField(max_length=50, required=False)
    city = forms.CharField(max_length=50, required=False)
    min_salary = forms.IntegerField(required=False)
    max_salary = forms.IntegerField(required=False)
    experience_level = forms.ChoiceField(
        choices=[
            ("intern", "intern"),
            ("junior", "junior"),
            ("mid", "mid"),
            ("senior", "senior"),
        ]
    )
