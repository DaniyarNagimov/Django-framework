# Generated by Django 3.2.9 on 2021-11-23 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20211117_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(default=18, verbose_name='возраст'),
        ),
    ]
