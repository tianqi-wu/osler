# Generated by Django 3.0.5 on 2020-08-06 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0009_auto_20200806_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='discreteresulttype',
            name='is_panic',
            field=models.CharField(choices=[('T', 'Abnormal value'), ('F', 'Normal value')], default='T', max_length=1),
        ),
    ]
