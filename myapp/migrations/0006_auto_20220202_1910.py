# Generated by Django 3.1.14 on 2022-02-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20220202_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='caste',
            field=models.FileField(blank=True, null=True, upload_to='d/3'),
        ),
    ]