# Generated by Django 3.0.3 on 2020-03-04 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_user_kakao_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='kakao_id',
            field=models.CharField(max_length=250, null=True),
        ),
    ]