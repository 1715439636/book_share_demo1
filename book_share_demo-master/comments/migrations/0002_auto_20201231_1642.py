# Generated by Django 2.2.2 on 2020-12-31 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]
