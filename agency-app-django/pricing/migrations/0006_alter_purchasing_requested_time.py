# Generated by Django 3.2.4 on 2022-04-12 00:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0005_alter_purchasing_plan_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasing',
            name='requested_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]