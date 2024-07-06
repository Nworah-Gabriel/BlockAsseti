"""
URL configuration for Asstesradar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BlockAssetiApp import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls import handler404

handler404 = views.custom_404_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_view),
    path("reg", views.reg),
    path("about", views.about),
    path("about_us", views.about),
    path("contact", views.contact),
    path("stocks", views.stocks),
    path("static/frontend/stocks", views.stocks),
    path("responsibility", views.responsibility),
    path("retirement_planning", views.retirement_planning),
    path("renewable_power", views.renewable_power),
    path("real_estate", views.real_estate),
    path("real-estate", views.real_estate),
    path("real_asset", views.real_assets),
    path("real-asset", views.real_assets),
    path("private_wealth", views.private_wealth),
    path("oil_gas", views.oil_gas),
    path("nfp", views.nfp),
    path("multi_asset", views.multi_assets),
    path("long_term", views.long_term),
    path("infrastructure", views.infrastructure),
    path("forex", views.forex),
    path("fixed", views.fixed_income),
    path("financial_planning", views.fincancial_planning),
    path("estate_planning", views.estate_planning),
    path("crypto", views.crypto),
    path("business_service", views.business_services),
    path("blog", views.blog),
    path("alternatives", views.alternatives),
    path("agriculture", views.agriculture),

    #---USER URL MAP--#
    path('register', views.Register.as_view(), name='Register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout),
    path('accounts/login/', views.user_login, name='login'),
    path('dashboard', views.Dashboard.as_view(), name='dashboard'),
    path("dashboard/id-verification", views.id_verification, name='id-verification'),
    path("deposit", views.deposit),
    path("tradinghistory", views.trading_history),
    path("support", views.support),
    path("subtrade", views.subtrade),
    path("referuser", views.refer_user),
    path("asset-balance", views.asset_balance),
    path("buy-plan", views.buy_plan),
    path("accounthistory", views.account_history),
    path("account_setting", views.account_setting),
    path("email-verification", views.email_verification_1, name='email-verification'),
    path("email-verify", views.email_verification_2, name='email-verify'),
    path("forgot-password", views.forgot_password, name='forgot-password'),
    path("id-verification", views.id_verification, name='id-verification'),
    path("verify_account", views.id_verification, name='id-verification'),
    path("success", views.id_verification2, name='success'),
    path("withdrawals", views.withdraw, name='withdrawals'),
    path("withdrawal", views.withdraw, name='withdrawal'),
    path("verification-failed", views.id_verification_failure, name='failed'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('ref/<str:ref_email>/<str:ref_username>', views.ReferralRegister.as_view(), name='ref'),
    path('swap-crypto', views.swap_crypto, name='swap'),



   

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)