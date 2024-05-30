# Generated by Django 3.2.9 on 2024-05-30 09:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('problems', 'Problems'), ('general_info', 'General Information'), ('work_with_us', 'Work with Us'), ('product_info', 'Product Information')], max_length=50)),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(500)])),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
