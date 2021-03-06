# Generated by Django 2.2.4 on 2019-08-12 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kvkey',
            name='blank',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kvkey',
            name='default',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='kvkey',
            name='help_text',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='kvkey',
            name='name',
            field=models.CharField(default='Name', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kvkey',
            name='null',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
