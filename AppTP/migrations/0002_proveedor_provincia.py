# Generated by Django 4.0.1 on 2022-02-13 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='provincia',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
