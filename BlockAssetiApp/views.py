from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import User, ContactMessage, DepositHistory, WithdrawalHistory, TradingHistory, Referral
from django.contrib.auth.models import User as theUSer
# from .forms import UserForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from django.urls import reverse
from sqlite3 import IntegrityError

from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
from django.template.loader import get_template, render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model

#modules for mailing
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



# Create your views here.
def home_view(request):
    """
    A functional based view for the home page
    """

    return render(request, "index.html")

def reg(request):
    """
    A functional based view that directs the user to the main register page
    """

    return render(request, 'register.html')

def about(request):
    """
    A functional based view for the about page
    """

    return render(request, 'about-us.html') 

def contact(request):
    """
    A functional based view for the contact page
    """

    if request.method == 'POST':
        try:
            # Additional logic for handling POST requests
            form_data = request.POST
            first_name = form_data.get('First-Name')
            last_name = form_data.get('Last-Name')
            email = form_data.get('Email')
            mobile_no = form_data.get('Phone')
            message = form_data.get('Message')

            #create new contact message
            new_message = ContactMessage()
            ContactMessage.first_name = first_name
            ContactMessage.last_name = last_name
            ContactMessage.email = email
            ContactMessage.phone = mobile_no
            ContactMessage.message_body = message
            
            #save new user data
            new_message.save()
            print(new_message)
            return render(request, 'contact.html', {"message": "Message successfully sent",
                                                    "success":True,"domain":get_current_site(request).domain,
                                                    "protocol": 'https' if request.is_secure() else 'http'
                                                    })   
        except:
            return render(request, 'contact.html', {"message": "Oops! we didn't recieve your message, fill the form properly",
                                                    "success": False, "domain":get_current_site(request).domain,
                                                    "protocol": 'https' if request.is_secure() else 'http'})


    return render(request, 'contact.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})

def stocks(request):
    """
    A functional based view for the stock page
    """

    return render(request, 'stocks.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})

def responsibility(request):
    """
    A function based view for the responsibility page
    """

    return render(request, 'responsibility.html')

def retirement_planning(request):
    """
    A functional based view for the retirement planning page
    """

    return render(request, 'retirement-planning.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})

def renewable_power(request):
    """
    A functional based view for the renewable-power page
    """

    return render(request, 'renewable-power.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})

def real_estate(request):
    """
    A functional based view for displaying the real estate page
    """

    return render(request, 'real-estate.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})

def real_assets(request):
    """
    A functional based view for displaying the real asset page
    """

    return render(request, 'real-asset.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})

def private_wealth(request):
    """
    A functional based view for displaying the private wealth page
    """

    return render(request, 'private-wealth.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def oil_gas(request):
    """
    A functional based view for displaying the oil and gas page
    """

    return render(request, 'oil-and-gas.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def nfp(request):
    """
    A functional based view for displaying the nfp page
    """

    return render(request, 'nfp.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def multi_assets(request):
    """
    A functional based view for displaying the multi assets page
    """

    return render(request, 'multi-asset.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def long_term(request):
    """
    A functional based view for displaying the long term page
    """

    return render(request, 'long-term.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def infrastructure(request):
    """
    A functional based view for displaying the infrastructure page
    """

    return render(request, 'infrastructure.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def forex(request):
    """
    A functional based view for displaying the forex page
    """

    return render(request, 'forex.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def fixed_income(request):
    """
    A functional based view for displaying the fixed income page
    """

    return render(request, 'fixed-income.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def fincancial_planning(request):
    """
    A functional based view for displaying the financial planning page
    """

    return render(request, 'financial-planning.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})



def estate_planning(request):
    """
    A functional based view for displaying the estate planning page
    """

    return render(request, 'estate-planning.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def crypto(request):
    """
    A functional based view for displaying the crypto page
    """

    return render(request, 'crypto.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def business_services(request):
    """
    A functional based view for displaying the business services page
    """

    return render(request, 'business-service.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def blog(request):
    """
    A functional based view for displaying the blog page
    """

    return render(request, 'blog.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def alternatives(request):
    """
    A functional based view for displaying the alternative page
    """

    return render(request, 'alternatives.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def agriculture(request):
    """
    A functional based view for displaying the agriculture page
    """

    return render(request, 'agriculture.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def trading_history(request):
    """
    A functional based view for the trading history page
    """
    try:
        #get user
        user = request.user
        user_query = User.objects.get(email=user.email)
        plan_history = user_query.profit_record.all()
    except:
        pass

    return render(request, "user/dashboard/tradinghistory.html", {"plan_history": plan_history, "domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def support(request):
    """
    A functional based view for the support page
    """

    return render(request, "user/dashboard/support.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})

def subtrade(request):
    """
    A functional based view for the subtrade page
    """

    return render(request, "user/dashboard/subtrade.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def refer_user(request):
    """
    A functional based view for the user referral page
    """
    user = ""
    try:
        user = User.objects.get(username=request.user.username)
        referals = user.referrals.all()
    except:
        pass

    return render(request, "user/dashboard/referuser.html", {"refs": referals, "domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})



def asset_balance(request):
    """
    A functional based view for the user asset balance page
    """

    return render(request, "user/dashboard/asset-balance.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def buy_plan(request):
    """
    A functional based view for the plan page
    """
    if request.method == "POST":
        try:
            user = request.user
            plan_data = request.POST
            amount = plan_data.get("iamount")
            duration = plan_data.get("duration")
            plan = plan_data.get("plan")
            # print(amount, duration, plan)

            #make a database query
            user_data = User.objects.get(email=user.email)

            #subtract from the user balance
            user_data.balance = user_data.balance - int(amount)

            if user_data.balance < 0:
                return render(request, "user/verification/history/low_balance.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})
            else:
                user_data.save()
            print(user_data.balance)

            #create trading history query
            new_trade = TradingHistory.objects.create()
            new_trade.Amount = amount
            new_trade.Duration = duration
            new_trade.plan = plan

            
            #saving and adding to the user list
            new_trade.save()
            user_data.profit_record.add(new_trade)
            return render(request, "user/verification/history/success.html", {"amount": amount, "domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})
        except:
            return render(request, "user/verification/history/failure.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


    return render(request, "user/dashboard/buy-plan.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def account_history(request):
    """
    A functional based view for the plan page
    """
    
    user = ""
    try:
        user = request.user

        User_query = User.objects.get(username=user.username, password=user.password, email=user.email)
        deposits = User_query.trading_history.all()

        #withdrawal history
        withdrawal_history = User_query
        withdrawal = User_query.withdrawal_history.all()
    except:
        pass

    return render(request, "user/dashboard/accounthistory.html", {"deposits": deposits, "Withdrawals": withdrawal, "domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def account_setting(request):
    """
    A functional based view for the plan page
    """

    if request.method == "POST":
        user = request.user
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        dob = data.get("dob")
        country= data.get("country")
        address = data.get("address")
        try:
            user_query = User.objects.get(username=user.username)
            user_query.fullname = name
            user_query.mobile_no = phone
            user_query.dob = dob
            user_query.country = country
            user_query.address
            user_query.save()
            print("personal settings sucessfully submitted")
            print(name, email)

        except:
            pass
    if request.method == "POST":
        try:
                name = data.get("name")
                bank_name = data.get("bank_name")
                account_name = data.get("account_name")
                account_no = data.get("account_no")
                swiftcode = data.get("swiftcode")
                btc_address= data.get("btc_address")
                ltc_address= data.get("ltc_address")
                eth_address= data.get("eth_address")

                user_query = User.objects.get(username=user.username)
                user_query.bank_name = bank_name
                user_query.account_name = account_name
                user_query.account_no = account_no
                user_query.swiftcode = swiftcode
                user_query.btc_address = btc_address
                user_query.ltc_address = ltc_address
                user_query.eth_address = eth_address
                user_query.save()
                print("withdrawal settings sucessfully submitted")

        except:
                pass
    if request.method == "POST":
        
        current_password = data.get("current_password")
        password = data.get("password")
        password_confirmation = data.get("password_confirmation")   
        try:
            user_query = User.objects.get(username=user.username)
            if str(user.password) == str(current_password):
                print("accurate:", current_password)
                if str(password) == str(password_confirmation):
                    user_query.password = password
                    user_query.save()
                    print("password settings sucessfully submitted")
        except:
            pass
       


    return render(request, "user/dashboard/account-settings.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def email_verification_1(request):
    """
    A functional based view for the email verification 1 page
    """

    return render(request, "user/verify-email.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})

def email_verification_2(request):
    """
    A functional based view for the email verifiction 2 page
    """

    return render(request, "user/verification/verify.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})

def id_verification(request):
    """
    A functional based view for the id verification page
    """

    if request.method == 'POST':
        try:
            print("posted")
            user = request.user
            user_id = request.POST
            
            front_image = request.FILES['pics1']
            back_image = request.FILES['pics2']
            print(f"Front view: {front_image}  Back view: {back_image}")

            #confirm the user
            get_user = User.objects.get(username=user.username, password=user.password, unique_id = user.unique_id)
            get_user.verified = True
            get_user.ID_front = front_image
            get_user.ID_back = back_image
            get_user.save()
            print(get_user)
            return redirect('success')
        except:
            return redirect('failed')

    return render(request, "user/verification/id_verification.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def id_verification2(request):
    """
    A functional based view for the id verification page
    """

    return render(request, "user/verification/success.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


def id_verification_failure(request):
    """
    A functional based view for the id verification page
    """

    return render(request, "user/verification/failure.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


    # return render(request, "user/verification/id_verification.html")


def forgot_password(request):
    """
    A functional based view for the plan page
    """
    
    return render(request, "user/forgot-password.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})

def custom_404_view(request, exception):
    return render(request, '404.html', {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'}, status=404)


class ReferralRegister(TemplateView):
    template_name = 'user/register.html'
    new_user = ""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_variable'] = 'Hello, World!'
        return context

    def get(self, request, *args, **kwargs):    
        # Additional logic for handling GET requests
        return super().get(request, *args, **kwargs)

    def post(self, request, ref_email, ref_username):
        try:
            # Additional logic for handling POST requests
            form_data = request.POST
            username = form_data.get('username')
            fullname = form_data.get('name')
            email = form_data.get('email')
            mobile_no = form_data.get('phone')
            password = form_data.get('password')
            country = form_data.get('country')

            #create new user
            new_user = User()
            new_user.username = username
            new_user.fullname = fullname
            new_user.email = email
            new_user.mobile_no = mobile_no
            new_user.password = password
            new_user.country = country
            new_user.balance = 0
            new_user.deposit = 0
            new_user.profit = 0
            new_user.referre = ref_email

            #create new referral
            referral = Referral.objects.create()
            referral.name = ref_email
            referral.verified = False
            referral.save()

            referre = User.objects.get(email=ref_email)
            referre.referrals.add(referral)
        except:
            pass

        #save new user data
        # try:
        new_user.save()
        # except:
            # return render(request, 'user/register.html')

        #get the user and redirect to the dashboard with the data
        # user = User.objects.get(username=username, password=password)

        activateEmail(self.request,new_user,new_user.email)
        return redirect('email-verification')
        # return HttpResponse('Sucessfully Registered')

class Register(TemplateView):
    template_name = 'user/register.html'
    new_user = ""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_variable'] = 'Hello, World!'
        return context

    def get(self, request, *args, **kwargs):    
        # Additional logic for handling GET requests
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            # Additional logic for handling POST requests
            form_data = request.POST
            username = form_data.get('username')
            fullname = form_data.get('name')
            email = form_data.get('email')
            mobile_no = form_data.get('phone')
            password = form_data.get('password')
            country = form_data.get('country')

            #create new user
            new_user = User()
            new_user.username = username
            new_user.fullname = fullname
            new_user.email = email
            new_user.mobile_no = mobile_no
            new_user.password = password
            new_user.country = country
            new_user.balance = 0
            new_user.deposit = 0
            new_user.profit = 0
        except:
            pass

        #save new user data
        try:
            new_user.save()
        except:
            return render(request, 'user/register.html', {"message":"User details already exist!", "success":False, "domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})

        #get the user and redirect to the dashboard with the data
        # user = User.objects.get(username=username, password=password)

        activateEmail(self.request,new_user,new_user.email)
        return redirect('email-verification')
        # return HttpResponse('Sucessfully Registered')


def user_login(request):
    error = ""
    email = ""
    password = ""
    user = ""
    if request.method == 'POST':
        user = request.POST
        email = user.get('email')
        password = user.get('password')
        try:
            user =  User.objects.get(email=email, password=password)
        except:
            user = ""
        # user = authenticate(request, email=email, password=password,)
        print(f'USER: {email} {password}')
        print(user)
    # if user is not None:
        # Specify the authentication backend here
        if user:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('dashboard')
        else:
            # Handle authentication failure
            return render(request, 'user/login.html', {"message": "Invalid Login Details", "success":False, "domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})
    return render(request, 'user/login.html', {"domain":get_current_site(request).domain})  # Replace 'login.html' with the name of your login template

def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login') 

def clear_cookies(request):
    response = HttpResponseRedirect('cookies cleared')  # Redirect to any page after clearing cookies
    response.delete_cookie('cookie_name')  # Replace 'cookie_name' with the name of the cookie you want to clear
    return response


class Dashboard(LoginRequiredMixin, View):
    template_name = 'user/dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_variable'] = 'Hello, World!'
        return context

    def get(self, request, *args, **kwargs):
        # Additional logic for handling GET requests
        user = request.user
        # Your logic to retrieve data
        return render(request, 'user/dashboard/dashboard.html', {'user': user, "domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})

        # return render(request, 'user/dashboard/dashboard.html', )

    def post(self, request, *args, **kwargs):
        # Additional logic for handling POST requests
        user = request.user
        return render(request, 'user/dashboard/dashboard.html', {'user': user, "domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})
    

def deposit(request):
    """
    A functional based view for the deposit page
    """
    if request.method == 'POST':
        new_deposit = request.POST
        amount = new_deposit.get("amount")
        method = new_deposit.get("payment_method")
        token = new_deposit.get("_token")

        try:
            create_deposit = DepositHistory.objects.create()
            create_deposit.Amount = str(amount)
            create_deposit.Method = method
            create_deposit.TOken = token
            create_deposit.Payment_proof = request.FILES['pics1']
            #get user details
            user = request.user
            get_user = User.objects.get(username=user.username, password=user.password, unique_id = user.unique_id)
            #save the newly created deposit
            create_deposit.save()
            print(create_deposit)
            get_user.trading_history.add(create_deposit)
            # get_user.balance += int(amount)
            get_user.save()
            return render(request, "user/verification/deposit/success.html", {"amount":amount, "domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})
        except:
            return render(request, "user/verification/deposit/low_balance.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})


    return render(request, "user/dashboard/deposits.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})



def withdraw(request):
    """
    A functional based view for the withdraw page
    """
    if request.method == 'POST':
        withrawal_request = request.POST
        amount = withrawal_request.get("amount")
        wallet_address = withrawal_request.get("Wallet_address")
        token = withrawal_request.get("_token")
        withdrawal_message = withrawal_request.get("withdrawal_message")

       
        create_withdrawal = WithdrawalHistory.objects.create()
        create_withdrawal.Amount = str(amount)
        create_withdrawal.wallet_address = wallet_address
        create_withdrawal.TOken = token
        create_withdrawal.withdrawal_message = withdrawal_message
        #get user details
        user = request.user
        get_user = User.objects.get(username=user.username, password=user.password, unique_id = user.unique_id)

        new_amount = int(user.balance) - int(amount)
        if new_amount < 0:
            return render(request, "user/verification/withdraw/low_balance.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})
        else:
            get_user.balance = str(amount)
            #save the newly created deposit
            create_withdrawal.save()
            print(create_withdrawal)
            get_user.withdrawal_history.add(create_withdrawal)
            get_user.save()
        return render(request, "user/verification/withdraw/success.html", {"amount":amount, "domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})

            
    return render(request, "user/dashboard/withdraw.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})






def swap_crypto(request):



    return render(request, "user/dashboard/swap.html", {"domain":get_current_site(request).domain, "protocol": 'https' if request.is_secure() else 'http'})



class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp)  + six.text_type(user.is_active)
        )

account_activation_token = AccountActivationTokenGenerator()

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    try:
        if user and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()

            messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
            return redirect('login')
        else:
            messages.error(request, 'Activation link is invalid!')
    except:
        pass
    
    return redirect('login')




"""A module for Bhulkee automated script in form of OOP"""


class BulkMailer():
    """A class that handles the sending of emails"""
    
    #SOME IMPORTANT VARIABLES#
    SERVER = 'mail.privateemail.com'
    FROM = 'support@blockasseti.com'
    PASS = 'blockasset'
    

    def __init__(self):
        """A constructor for the Bulkmailer class"""

        self.heading = ""
        self.body = ""
        self.email_list = ["gabrielnworah6@gmail.com"]

    def AppendMailAddress(self, maillist):
        """A method that appends emails in the mailist to the mail_list attribute"""
        
        if maillist == None:
            return None
        for mail in maillist:
            self.email_list.append(maillist)
        return

    def compose(self):
        """A method that composes the email heading and body"""

        msg = MIMEMultipart()
        msg['Subject'] = self.heading
        msg['From'] = self.FROM
        msg.attach(MIMEText(self.body, 'html'))
        return msg
    
    def initializeAndSend(self):
        """A method to initialize the mail server and sends the email to the reciepient"""
        
        message = self.compose()
        try:
            server = smtplib.SMTP_SSL(self.SERVER)
        except Exception:
            return None
        server.set_debuglevel(0)
        server.ehlo()
        server.login(self.FROM, self.PASS)
        if self.email_list != None:
            for mail_address in self.email_list:
                server.sendmail(self.FROM, mail_address, message.as_string())

        else:
            return False
        server.quit()
        return True




def activateEmail(request, user, to_email):


    mail = BulkMailer()
    content = {
        'image_url': '/static/img/logo.png',
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    }
    mail.heading = 'Activate Your Account.'
    mail.body = get_template('user/verification/verify.html').render(content)
    mail.compose()
    mail.email_list.append(to_email)
    mail.email_list.append('gabrielnworah6@gmail.com')
    mail.initializeAndSend()

    
    if mail:
        messages.success(request, f'Dear <b>{user.username}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')

