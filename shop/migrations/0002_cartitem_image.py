# Generated by Django 4.2.3 on 2023-08-13 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='image',
            field=models.ImageField(default=1, upload_to='item_images/'),
            preserve_default=False,
        ),
    ]
