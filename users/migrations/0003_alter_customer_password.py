# Generated by Django 3.2.9 on 2021-12-12 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customer_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
