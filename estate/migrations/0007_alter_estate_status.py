# Generated by Django 3.2.7 on 2021-09-09 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0006_estate_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='status',
            field=models.CharField(choices=[('رهن', 'رهن'), ('اجاره', 'اجاره'), ('فروش', 'فروش')], max_length=10, verbose_name='وضعیت'),
        ),
    ]
