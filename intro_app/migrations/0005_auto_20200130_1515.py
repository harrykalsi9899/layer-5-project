# Generated by Django 3.0.2 on 2020-01-30 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intro_app', '0004_auto_20200130_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='intro_app.Address'),
        ),
    ]
