# Generated by Django 2.2.8 on 2019-12-21 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191221_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='graphic_card_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='memory1_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='memory2_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='memory3_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='memory4_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='motherboard_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='processor_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]