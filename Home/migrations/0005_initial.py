# Generated by Django 4.1.13 on 2024-02-27 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0004_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='userAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=12, null=True)),
                ('token', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
