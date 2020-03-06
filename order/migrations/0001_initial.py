# Generated by Django 3.0.3 on 2020-03-06 00:55

from django.db import migrations, models
import django.db.models.deletion
import order.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.IntegerField(null=True)),
                ('is_shipping_address', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=45, null=True)),
                ('last_name', models.CharField(max_length=45, null=True)),
                ('address_1', models.CharField(max_length=200, null=True)),
                ('address_2', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User')),
            ],
            options={
                'db_table': 'billing_addresses',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_code', models.CharField(max_length=45, null=True, unique=True)),
                ('discount_rate', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('is_used', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'coupons',
            },
        ),
        migrations.CreateModel(
            name='PackageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(max_length=45, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
            options={
                'db_table': 'package_types',
            },
        ),
        migrations.CreateModel(
            name='PaymentOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'payment_options',
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User')),
            ],
            options={
                'db_table': 'wishlists',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('is_closed', models.BooleanField(default=False)),
                ('billing_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.BillingAddress')),
                ('coupon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Coupon')),
                ('package_type', models.ForeignKey(default=order.models.get_package_type, on_delete=django.db.models.deletion.CASCADE, to='order.PackageType')),
                ('payment_option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.PaymentOption')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User')),
            ],
            options={
                'db_table': 'carts',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=100, unique=True)),
                ('card_holder', models.CharField(max_length=100)),
                ('expiration_year', models.CharField(max_length=10)),
                ('expiration_month', models.CharField(max_length=10)),
                ('cvv', models.CharField(max_length=100)),
                ('payment_option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.PaymentOption')),
            ],
            options={
                'db_table': 'cards',
            },
        ),
    ]
