# Generated by Django 3.2.4 on 2022-04-11 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchasing',
            old_name='catagory',
            new_name='plan_name',
        ),
    ]