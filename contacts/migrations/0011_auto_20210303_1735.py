# Generated by Django 3.1.5 on 2021-03-03 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0010_auto_20210303_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='category',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
