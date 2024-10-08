# Generated by Django 5.0.4 on 2024-04-24 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0002_product_image_alter_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('url_social_media', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
