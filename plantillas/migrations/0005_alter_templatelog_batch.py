# Generated by Django 3.2.18 on 2023-04-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantillas', '0004_auto_20230414_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatelog',
            name='batch',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]