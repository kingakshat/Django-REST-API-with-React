# Generated by Django 3.0.6 on 2021-07-15 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_api_app', '0020_auto_20210714_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='flight_two_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(default='Vistara', max_length=100)),
                ('s_n_d', models.CharField(default='Chennai -to- Las Vegas', max_length=100)),
                ('seat_name', models.CharField(max_length=100)),
                ('status', models.CharField(default='AVALIBLE', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='flight_one_db',
            name='booking_id',
        ),
        migrations.AddField(
            model_name='booking_db',
            name='f_name',
            field=models.CharField(default='--NA--', max_length=100),
        ),
        migrations.AddField(
            model_name='booking_db',
            name='s_n_d',
            field=models.CharField(default='--NA--', max_length=100),
        ),
        migrations.AddField(
            model_name='flight_one_db',
            name='f_name',
            field=models.CharField(default='Air India', max_length=100),
        ),
        migrations.AddField(
            model_name='flight_one_db',
            name='s_n_d',
            field=models.CharField(default='Mumbai -to- London', max_length=100),
        ),
    ]