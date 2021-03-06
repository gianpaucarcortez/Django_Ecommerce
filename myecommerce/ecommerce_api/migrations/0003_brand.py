# Generated by Django 3.2.9 on 2021-11-11 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_api', '0002_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='brands')),
                ('brand', models.CharField(max_length=200)),
                ('activated', models.BooleanField()),
            ],
        ),
    ]
