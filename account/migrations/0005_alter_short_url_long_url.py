# Generated by Django 4.0.4 on 2022-06-22 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_short_url_long_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='short_url',
            name='long_url',
            field=models.URLField(null=True, verbose_name='URL'),
        ),
    ]