# Generated by Django 3.0.5 on 2020-07-22 19:04

from django.db import migrations, models
import osler.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='name',
            field=models.CharField(max_length=100, validators=[osler.core.validators.validate_name]),
        ),
        migrations.AlterField(
            model_name='drugcategory',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, validators=[osler.core.validators.validate_name]),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, validators=[osler.core.validators.validate_name]),
        ),
        migrations.AlterField(
            model_name='measuringunit',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, validators=[osler.core.validators.validate_name]),
        ),
    ]