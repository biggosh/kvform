# Generated by Django 2.2.4 on 2019-08-12 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kvform', '0002_auto_20190812_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='kvkey',
            name='kv_form',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='kvform.KVForm'),
            preserve_default=False,
        ),
    ]