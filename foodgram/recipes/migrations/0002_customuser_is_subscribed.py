# Generated by Django 4.2.5 on 2023-09-20 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_subscribed',
            field=models.BooleanField(default=False),
        ),
    ]