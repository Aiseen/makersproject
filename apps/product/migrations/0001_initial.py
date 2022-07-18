# Generated by Django 4.0.6 on 2022-07-18 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('price', models.BigIntegerField(verbose_name='price')),
            ],
        ),
    ]
