# Generated by Django 3.0.8 on 2020-08-23 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0010_auto_20200823_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=350, null=True),
        ),
    ]
