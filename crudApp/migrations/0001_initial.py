# Generated by Django 5.2.3 on 2025-06-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('sname', models.CharField(max_length=50)),
                ('sclass', models.IntegerField()),
                ('saddress', models.CharField(max_length=100)),
            ],
        ),
    ]
