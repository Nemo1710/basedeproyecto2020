# Generated by Django 2.2.11 on 2020-03-30 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19', '0005_auto_20200330_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='casosporprovincia',
            name='Actualizado',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
