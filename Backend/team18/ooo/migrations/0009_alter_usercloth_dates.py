# Generated by Django 4.1.1 on 2022-11-21 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ooo", "0008_alter_usercloth_dates"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usercloth", name="dates", field=models.TextField(null=True),
        ),
    ]