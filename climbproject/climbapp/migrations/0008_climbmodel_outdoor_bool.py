# Generated by Django 2.1.2 on 2018-11-20 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climbapp', '0007_remove_climbmodel_in_or_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='climbmodel',
            name='outdoor_bool',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
