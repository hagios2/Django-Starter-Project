# Generated by Django 3.0.6 on 2020-05-24 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default='This is a cool product'),
        ),
    ]
