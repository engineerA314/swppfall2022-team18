# Generated by Django 4.1.1 on 2022-12-04 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ooo", "0002_usercloth_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usercloth",
            name="image",
            field=models.ImageField(blank=True, default="", upload_to="userimages/"),
        ),
        migrations.AlterField(
            model_name="usercloth",
            name="image_link",
            field=models.CharField(max_length=1000),
        ),
    ]
