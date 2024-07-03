from django.contrib import admin
from .models import User, ContactMessage, DepositHistory, WithdrawalHistory, TradingHistory, Referral

# Register your models here.
admin.site.register(User)
admin.site.register(ContactMessage)
admin.site.register(DepositHistory)
admin.site.register(WithdrawalHistory)
admin.site.register(TradingHistory)
admin.site.register(Referral)

