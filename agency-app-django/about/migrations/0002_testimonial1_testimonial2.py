# Generated by Django 3.1.7 on 2021-04-14 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='testimonials')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=264)),
            ],
        ),
    ]
