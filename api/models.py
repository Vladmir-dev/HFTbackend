from django.db import models
from django.contrib.auth.models import User

ACCOUNTS = (
    ('paper_account', 'Paper Account'),
    ('live_account', 'Live Account'),
)

COUNTRIES = (
    ('uganda', 'Uganda'),
    ('kenya', 'Kenya'),
    ('tanzania', 'Tanzania'),
    ('rwanda', 'Rwanda'),
    ('burundi', 'Burundi'),
    ('south_sudan', 'South Sudan'),
)

CITIES = (
    ('kampala', 'Kampala'),
    ('Mbarara', 'Mbarara'),
    ('Gulu', 'Gulu'),
    ('dar_es_salaam', '	Dar es Salaam'),
    ('mwanza', 'Mwanza'),
    ('arusha', 'Arusha'),
    ('nairobi', 'Nairobi'),
    ('kisumu', 'Kisumu'),
    ('mombasa', 'Mombasa'),
    ('kigali', 'Kigali'),
    ('butare', 'Butare'),
    ('gitarama', 'Gitarama'),
    ('bujumbura', 'Bujumbura'),
    ('gitega', 'Gitega'),
    ('muyinga', 'Muyinga'),
)

class Profile(models.Model):
    account_type = models.CharField(max_length=100, choices=ACCOUNTS, blank=True)
    mobile_number = models.IntegerField(unique=True)
    country_of_residence = models.CharField(max_length=100, choices=COUNTRIES, blank=True)
    city = models.CharField(max_length=100, choices=CITIES, blank=True)
    zip_code = models.IntegerField()
    user = models.ForeignKey(
        User, related_name="profiles", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.account_type

class Algo(models.Model):
    symbol = models.CharField(max_length=5)
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey(
        User, related_name="algo", on_delete=models.CASCADE, null=True
    )

    def __str__(self) -> str:
        return self.symbol

