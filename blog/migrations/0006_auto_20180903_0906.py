# Generated by Django 2.0.8 on 2018-09-03 08:06

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180831_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
