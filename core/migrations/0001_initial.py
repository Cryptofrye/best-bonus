# Generated by Django 3.0 on 2020-01-16 01:00

import core.models
import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='casino_logos/', verbose_name='Suplier image')),
                ('ca_license_bool', models.BooleanField(default=False, verbose_name='License')),
                ('suplier_type', models.IntegerField(choices=[(0, 'Casino'), (1, 'Betting'), (2, 'CS:GO')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('two_word_desc', models.CharField(max_length=300, verbose_name='About the bonus in 2 words')),
                ('bonus_digit', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000000)], verbose_name='Bonus value')),
                ('bonus_desc', models.TextField(blank=True, max_length=1500, null=True, verbose_name='Bonus description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='bonus_images/', verbose_name='Bonus image')),
                ('dep_bool', models.BooleanField(default=True)),
                ('dep', models.PositiveSmallIntegerField()),
                ('doa', models.DateField(default=datetime.date.today, verbose_name='Date of adding')),
                ('doe', models.DateField(default=core.models.today_plus_30_days, verbose_name='Date of expiring')),
                ('wager', models.SmallIntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Bonus wager')),
                ('bonus_type', models.IntegerField(choices=[(0, 'Deposit'), (1, 'Freespin')], default=0)),
                ('suplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Suplier')),
            ],
            options={
                'ordering': ['-bonus_digit'],
            },
        ),
    ]