# Generated by Django 5.0 on 2024-01-16 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='One',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('bio', models.TextField()),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='index/img')),
            ],
        ),
    ]
