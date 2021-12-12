# Generated by Django 3.2.4 on 2021-06-30 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='webiste',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
