# Generated by Django 2.1.1 on 2018-09-30 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performer',
            name='is_band',
            field=models.BooleanField(choices=[['individual', False], ['band', True]], default=False, verbose_name="It's a band"),
        ),
    ]