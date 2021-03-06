# Generated by Django 2.1 on 2022-02-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.TextField(blank=0, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PayWay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('TG', 'TigoPesa'), ('MP', 'M-Pesa'), ('TP', 'T-Pesa'), ('PP', 'PayPal')], max_length=100)),
                ('amount', models.FloatField(blank=1, max_length=100)),
                ('time', models.IntegerField(max_length=100)),
                ('customer_name', models.TextField(max_length=225)),
                ('course_name', models.TextField(max_length=100)),
            ],
        ),
    ]
