# Generated by Django 3.1.14 on 2022-02-02 13:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20220202_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='caste',
            field=models.FileField(blank=True, default=django.utils.timezone.now, upload_to='d/3'),
            preserve_default=False,
        ),
    ]
