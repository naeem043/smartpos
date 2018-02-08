# Generated by Django 2.0.1 on 2018-02-06 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=100)),
                ('url', models.CharField(blank=True, max_length=100)),
                ('module', models.CharField(blank=True, max_length=100)),
                ('page_name', models.CharField(blank=True, max_length=100)),
                ('parent', models.IntegerField(blank=True)),
                ('menu_order', models.IntegerField(blank=True)),
                ('status', models.BooleanField(default=1)),
            ],
        ),
    ]
