# Generated by Django 4.0.2 on 2022-02-18 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('mileage', models.IntegerField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vehicleApi.vehicle')),
            ],
        ),
        migrations.DeleteModel(
            name='Mileage_History',
        ),
    ]
