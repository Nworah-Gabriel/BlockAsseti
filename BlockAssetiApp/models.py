from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from uuid import uuid4
from datetime import datetime
# Create your models here.

class User(AbstractUser):
    """
    A class model for storing the user's data
    """

    
    fullname = models.CharField(max_length=200, default="Anonymous", null=True)
    mobile_no = models.CharField(max_length=100, default="09000000000", null=True)
    country = models.CharField(max_length=100, default="unknown", null=True)
    balance = models.IntegerField(default=0, null=True)
    deposit = models.IntegerField(default=0, null=True)
    bonus = models.IntegerField(default=0, null=True)
    profit = models.IntegerField(default=0, null=True)
    unique_id = models.UUIDField(unique=True, primary_key=True, default=uuid4)
    verified = models.BooleanField(default=False)
    ID_verified = models.BooleanField(default=False)
    ID_front = models.ImageField(upload_to='static/uploaded', null=True, blank=True)
    ID_back = models.ImageField(upload_to='static/uploaded', null=True, blank=True)
    trading_history = models.ManyToManyField(to="DepositHistory", null=True, blank=True)
    withdrawal_history = models.ManyToManyField(to="WithdrawalHistory", null=True, blank=True)
    profit_record = models.ManyToManyField(to="TradingHistory", null=True, blank=True)
    referre = models.CharField(max_length=200, default="Anonymous")
    referrals = models.ManyToManyField(to="Referral", null=True, blank=True)
    dob = models.CharField(max_length=50,null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    bank_name = models.CharField(max_length=100,null=True, blank=True)
    account_name = models.CharField(max_length=100,null=True, blank=True)
    account_no = models.CharField(max_length=50,null=True, blank=True)
    swiftcode = models.CharField(max_length=100,null=True, blank=True)
    btc_address = models.CharField(max_length=200,null=True, blank=True)
    eth_address = models.CharField(max_length=200,null=True, blank=True)
    ltc_address = models.CharField(max_length=200,null=True, blank=True)
    total_bonus = models.CharField(max_length=200,null=True, blank=True)
    Active_Investment_Plans = models.BigIntegerField(max_length=200, default=0, null=True, blank=True)
    Total_Investment_Plans = models.BigIntegerField(max_length=200, default=0, null=True, blank=True)
    Total_deposit = models.BigIntegerField(max_length=200, default=0, null=True, blank=True)
    Total_withdrawal = models.BigIntegerField(max_length=200, default=0, null=True, blank=True)
    Edited_Personal_Settings = models.BooleanField(default=False)
    Edited_Withdrawal_Settings = models.BooleanField(default=False)
    Edited_security_Settings = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class ContactMessage(models.Model):
    """
    A class based model for storing messages gotten from the contact form
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message_body = models.TextField()
    

    def __str__(self):
        """
        A string representation of the data stored in the database
        """

        return self.first_name

class Referral(models.Model):
    """
    A class based model for storing user's trading history
    """

    name = models.CharField(max_length=50, null=True)
    verified = models.BooleanField(null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        A string representation of the data stored in the database
        """

        return self.name

class TradingHistory(models.Model):
    """
    A class based model for storing user's trading history
    """

    plan = models.CharField(max_length=50, null=True)
    Amount = models.IntegerField(null=True)
    Duration = models.CharField(max_length=30, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        A string representation of the data stored in the database
        """

        return self.plan


class DepositHistory(models.Model):
    """
    A class based model for storing user's deposit history
    """

    Amount = models.CharField(max_length=50)
    Method = models.CharField(max_length=50)
    TOken = models.CharField(max_length=30)
    dateCreated = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    Payment_proof = models.ImageField(upload_to='static/uploaded', null=True, blank=True)
    def __str__(self):
        """
        A string representation of the data stored in the database
        """

        return self.Method

class WithdrawalHistory(models.Model):
    """
    A class based model for storing user's withdrawal history
    """

    Amount = models.CharField(max_length=50)
    wallet_address = models.CharField(max_length=200)
    TOken = models.CharField(max_length=30)
    dateCreated = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    withdrawal_message = models.CharField(max_length=50, default="Withdrawal Request")

    def __str__(self):
        """
        A string representation of the data stored in the database
        """

        return (f'{self.withdrawal_message}  {self.wallet_address}')

