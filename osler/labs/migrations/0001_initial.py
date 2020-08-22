# Generated by Django 3.0.5 on 2020-08-22 22:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_auto_20200822_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscreteMeasurementType',
            fields=[
                ('long_name', models.CharField(help_text='A unique name of the measurement', max_length=30, primary_key=True, serialize=False)),
                ('short_name', models.CharField(max_length=30)),
                ('order_index', models.PositiveIntegerField(default=0, help_text='Order at which this measurement will display')),
            ],
            options={
                'ordering': ['order_index'],
                'abstract': False,
            },
        ),
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
                ('measurement_type', models.ManyToManyField(to='labs.DiscreteMeasurementType')),
            ],
        ),
        migrations.AddField(
            model_name='discretemeasurementtype',
            name='lab_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labs.LabType'),
        ),
        migrations.CreateModel(
            name='DiscreteMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.Lab')),
                ('measurement_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labs.DiscreteMeasurementType')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labs.DiscreteResultType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContinuousMeasurementType',
            fields=[
                ('long_name', models.CharField(help_text='A unique name of the measurement', max_length=30, primary_key=True, serialize=False)),
                ('short_name', models.CharField(max_length=30)),
                ('order_index', models.PositiveIntegerField(default=0, help_text='Order at which this measurement will display')),
                ('unit', models.CharField(blank=True, max_length=15, null=True)),
                ('panic_upper', models.DecimalField(blank=True, decimal_places=1, help_text='All labs above this value will display as red with a warning sign. Will also be used as the upper bound of reference.', max_digits=5, null=True)),
                ('panic_lower', models.DecimalField(blank=True, decimal_places=1, help_text='All labs below this value will display as blue with a warning sign. Will also be used as the lower bound of reference.', max_digits=5, null=True)),
                ('lab_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labs.LabType')),
            ],
            options={
                'ordering': ['order_index'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContinuousMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=1, max_digits=5)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.Lab')),
                ('measurement_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labs.ContinuousMeasurementType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]