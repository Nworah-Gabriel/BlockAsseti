# Generated by Django 4.2.11 on 2024-07-03 21:59

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('message_body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DepositHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.CharField(max_length=50)),
                ('Method', models.CharField(max_length=50)),
                ('TOken', models.CharField(max_length=30)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('Payment_proof', models.ImageField(blank=True, null=True, upload_to='static/uploaded')),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('verified', models.BooleanField(null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TradingHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=50, null=True)),
                ('Amount', models.IntegerField(null=True)),
                ('Duration', models.CharField(max_length=30, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WithdrawalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.CharField(max_length=50)),
                ('wallet_address', models.CharField(max_length=200)),
                ('TOken', models.CharField(max_length=30)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('withdrawal_message', models.CharField(default='Withdrawal Request', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('fullname', models.CharField(default='Anonymous', max_length=200, null=True)),
                ('mobile_no', models.CharField(default='09000000000', max_length=100, null=True)),
                ('country', models.CharField(default='unknown', max_length=100, null=True)),
                ('balance', models.IntegerField(default=0, null=True)),
                ('deposit', models.IntegerField(default=0, null=True)),
                ('bonus', models.IntegerField(default=0, null=True)),
                ('profit', models.IntegerField(default=0, null=True)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('verified', models.BooleanField(default=False)),
                ('ID_verified', models.BooleanField(default=False)),
                ('ID_front', models.ImageField(blank=True, null=True, upload_to='static/uploaded')),
                ('ID_back', models.ImageField(blank=True, null=True, upload_to='static/uploaded')),
                ('referre', models.CharField(default='Anonymous', max_length=200)),
                ('dob', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('account_name', models.CharField(blank=True, max_length=100, null=True)),
                ('account_no', models.CharField(blank=True, max_length=50, null=True)),
                ('swiftcode', models.CharField(blank=True, max_length=100, null=True)),
                ('btc_address', models.CharField(blank=True, max_length=200, null=True)),
                ('eth_address', models.CharField(blank=True, max_length=200, null=True)),
                ('ltc_address', models.CharField(blank=True, max_length=200, null=True)),
                ('total_bonus', models.CharField(blank=True, max_length=200, null=True)),
                ('Active_Investment_Plans', models.BigIntegerField(blank=True, default=0, max_length=200, null=True)),
                ('Total_Investment_Plans', models.BigIntegerField(blank=True, default=0, max_length=200, null=True)),
                ('Total_deposit', models.BigIntegerField(blank=True, default=0, max_length=200, null=True)),
                ('Total_withdrawal', models.BigIntegerField(blank=True, default=0, max_length=200, null=True)),
                ('Edited_Personal_Settings', models.BooleanField(default=False)),
                ('Edited_Withdrawal_Settings', models.BooleanField(default=False)),
                ('Edited_security_Settings', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='blockassetiapp_user_set', related_query_name='user', to='auth.group')),
                ('profit_record', models.ManyToManyField(blank=True, null=True, to='BlockAssetiApp.tradinghistory')),
                ('referrals', models.ManyToManyField(blank=True, null=True, to='BlockAssetiApp.referral')),
                ('trading_history', models.ManyToManyField(blank=True, null=True, to='BlockAssetiApp.deposithistory')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='blockassetiapp_user_permissions', related_query_name='user', to='auth.permission')),
                ('withdrawal_history', models.ManyToManyField(blank=True, null=True, to='BlockAssetiApp.withdrawalhistory')),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
