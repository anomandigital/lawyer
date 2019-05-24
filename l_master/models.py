from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from ClassicUserAccounts.models import SoftDeleteModel

User = get_user_model()


class Country(SoftDeleteModel):
    country_id = models.BigAutoField(primary_key=True)
    country_name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        db_table = "country"

    def __str__(self):
        return self.country_name


class State(SoftDeleteModel):
    state_id = models.BigAutoField(primary_key=True)
    state_name = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True, blank=True,
                                related_name='country_state')

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")
        db_table = "state"

    def __str__(self):
        return self.state_name


class City(SoftDeleteModel):
    city_id = models.BigAutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True, blank=True,
                                related_name='country_city')
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=True, blank=True,
                              related_name='country_state')
    city_name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _("City ")
        verbose_name_plural = _("Cities")
        db_table = "city"

    def __str__(self):
        return self.city_name


class Client(SoftDeleteModel):
    client_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.IntegerField(null=True, blank=True)
    about = models.CharField(max_length=500, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=False, blank=False,
                                related_name='country_client')
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=False, blank=False, related_name='state_client')
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=False, blank=False, related_name='city_client')
    address = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")
        db_table = "clients"

    def __str__(self):
        return str(self.client_id)

    def __int__(self):
        return self.client_id


class Court(SoftDeleteModel):
    court_id = models.BigAutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=False, blank=False,
                                related_name='country_court')
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=False, blank=False, related_name='country_court')
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=False, blank=False, related_name='city_court')
    address = models.TextField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = _("court")
        verbose_name_plural = _("courts")
        db_table = "court"

    def __str__(self):
        return str(self.court_id)

    def __int__(self):
        return self.court_id


class Case(SoftDeleteModel):
    case_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=500, null=False, blank=False)
    no = models.CharField(max_length=100, null=False, blank=False)
    filing_date = models.DateTimeField(null=True, blank=True)
    next_listing_date = models.DateTimeField(null=True, blank=True)
    last_listing_date = models.DateTimeField(null=True, blank=True)
    court = models.ForeignKey(Court, on_delete=models.PROTECT, null=True, blank=True, related_name='court_case')
    user = models.ForeignKey(User, related_name='user_case', null=True, blank=True, on_delete=models.PROTECT)
    clients = models.ForeignKey(Client, related_name='case_client', null=True, blank=True, on_delete=models.PROTECT)
    total_fee = models.TextField(null=True, blank=True)
    received_fee = models.TextField(null=True, blank=True)
    due_fee = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Case")
        verbose_name_plural = _("Cases")
        db_table = "cases"

    def __str__(self):
        return str(self.case_id)

    def __int__(self):
        return self.case_id


class Notification(SoftDeleteModel):
    n_id = models.BigAutoField(primary_key=True)
    sent_on_date = models.DateTimeField(null=True, blank=True)
    sent = models.BooleanField(default=False)
    case = models.ForeignKey(Case, on_delete=models.PROTECT, null=True, blank=True, related_name='case_notification')
    next_listing_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _("notification")
        verbose_name_plural = _("notifications")
        db_table = "notification"

    def __str__(self):
        return str(self.n_id)

    def __int__(self):
        return self.n_id


class Profile(SoftDeleteModel):
    profile_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True, related_name='user_profile')
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    about = models.CharField(max_length=500, null=True, blank=True)
    experience = models.TextField(max_length=500, null=True, blank=True)
    location = models.TextField(max_length=30, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True, blank=True,
                                related_name='country_profile')
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=True, blank=True, related_name='state_profile')
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True, blank=True, related_name='city_profile')

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        db_table = "profiles"

    def __str__(self):
        return str(self.profile_id)

    def __int__(self):
        return self.profile_id