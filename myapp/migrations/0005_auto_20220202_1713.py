# Generated by Django 3.1.14 on 2022-02-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20220202_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_data',
            name='mark_graduation',
            field=models.FileField(blank=True, upload_to='d/7'),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='sign',
            field=models.ImageField(blank=True, upload_to='d/8'),
        ),
    ]