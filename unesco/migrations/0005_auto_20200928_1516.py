# Generated by Django 3.0.8 on 2020-09-28 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0004_auto_20200928_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]