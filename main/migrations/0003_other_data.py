# Generated by Django 4.2.dev20220803094251 on 2022-08-12 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_data_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Other_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('value', models.IntegerField()),
            ],
        ),
    ]
