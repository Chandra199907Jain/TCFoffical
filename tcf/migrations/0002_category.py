# Generated by Django 4.0.3 on 2022-03-28 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
    ]
