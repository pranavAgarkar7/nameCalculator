# Generated by Django 3.2.9 on 2021-11-07 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papp', '0002_remove_user_data_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]