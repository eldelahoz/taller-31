# Generated by Django 5.1 on 2024-08-31 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('statu_id', models.AutoField(primary_key=True, serialize=False)),
                ('statu_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
