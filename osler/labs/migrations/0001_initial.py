# Generated by Django 3.0.5 on 2020-08-13 03:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_auto_20200806_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('order_index', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['order_index'],
            },
        ),
        migrations.CreateModel(
            name='MeasurementType',
            fields=[
                ('long_name', models.CharField(help_text='A unique name of the measurement', max_length=30, primary_key=True, serialize=False)),
                ('short_name', models.CharField(max_length=30)),
                ('value_type', models.CharField(choices=[('Continuous', 'Numerical'), ('Discrete', 'Categorical')], max_length=15)),
                ('unit', models.CharField(blank=True, help_text='Leave blank if this measurement is categorical', max_length=15, null=True)),
                ('panic_upper', models.DecimalField(blank=True, decimal_places=1, help_text='All labs above this value will display as red with a warning sign. Will also be used as the upper bound of reference. Leave blank if this measurement is categorical', max_digits=5, null=True)),
                ('panic_lower', models.DecimalField(blank=True, decimal_places=1, help_text='All labs below this value will display as blue with a warning sign. Will also be used as the lower bound of reference. Leave blank if this measurement is categorical', max_digits=5, null=True)),
                ('order_index', models.PositiveIntegerField(default=0, help_text='Order at which this measurement will display')),
                ('lab_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labs.LabType')),
            ],
            options={
                'ordering': ['order_index'],
            },
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('lab_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labs.LabType')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Patient')),
            ],
            options={
                'ordering': ['-lab_time'],
            },
        ),
        migrations.CreateModel(
            name='DiscreteResultType',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('is_panic', models.CharField(choices=[('T', 'Abnormal value'), ('F', 'Normal value')], default='T', help_text='If abnormal, all labs with this value will display as red with a warning sign.', max_length=1)),
                ('measurement_type', models.ManyToManyField(to='labs.MeasurementType')),
            ],
        ),
        migrations.CreateModel(
            name='DiscreteMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.Lab')),
                ('measurement_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labs.MeasurementType')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labs.DiscreteResultType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContinuousMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=1, max_digits=5)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.Lab')),
                ('measurement_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labs.MeasurementType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]