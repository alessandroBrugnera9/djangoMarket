# Generated by Django 3.0 on 2019-12-03 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='minimunAge',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
