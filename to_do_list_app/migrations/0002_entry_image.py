# Generated by Django 4.2.7 on 2023-11-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
