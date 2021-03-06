# Generated by Django 3.0.5 on 2020-08-29 18:20

from django.db import migrations, models
import django.db.models.deletion
import osler.core.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrugCategory',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, validators=[osler.core.validators.validate_name])),
            ],
            options={
                'verbose_name_plural': 'drug categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, validators=[osler.core.validators.validate_name])),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MeasuringUnit',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, validators=[osler.core.validators.validate_name])),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[osler.core.validators.validate_name])),
                ('dose', models.FloatField()),
                ('stock', models.PositiveSmallIntegerField(default=0)),
                ('expiration_date', models.DateField(help_text='MM/DD/YYYY')),
                ('lot_number', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.DrugCategory')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Manufacturer')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.MeasuringUnit')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]