# Generated by Django 3.1.14 on 2022-02-03 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('fathers_name', models.CharField(max_length=100)),
                ('fathers_occupation', models.CharField(blank=True, max_length=30)),
                ('mothers_name', models.CharField(max_length=100)),
                ('mothers_occupation', models.CharField(blank=True, max_length=30)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=180)),
                ('city', models.CharField(max_length=180)),
                ('pin', models.PositiveIntegerField()),
                ('course', models.CharField(choices=[('B.tech', 'B.tech'), ('MBA', 'MBA'), ('BCA', 'BCA'), ('BBA', 'BBA'), ('Diploma', 'Diploma')], max_length=100)),
                ('mark10_obtained', models.PositiveIntegerField(blank=True, null=True)),
                ('mark10_total', models.PositiveIntegerField(blank=True, null=True)),
                ('mark12_obtained', models.PositiveIntegerField(blank=True, null=True)),
                ('mark12_total', models.PositiveIntegerField(blank=True, null=True)),
                ('mark_graduation_obtained', models.PositiveIntegerField(blank=True, null=True)),
                ('mark_graduation_total', models.PositiveIntegerField(blank=True, null=True)),
                ('department', models.CharField(blank=True, choices=[('MBA department', 'MBA department'), ('Computer Science department', ' Computer Science department'), ('Electrical department', 'Electrical department'), ('Mechanical Department', 'Mechanical Department'), ('Civil Department', 'Civil Department'), ('Electronics and Engineering Department', 'Electronics and Engineering Department')], max_length=50)),
                ('mobile', models.PositiveIntegerField()),
                ('mobile2', models.PositiveIntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='d/1')),
                ('sign', models.ImageField(blank=True, upload_to='d/8')),
                ('Adhaar', models.FileField(blank=True, upload_to='d/2')),
                ('Adhaar_no', models.CharField(blank=True, max_length=12, null=True)),
                ('pan', models.FileField(blank=True, upload_to='d/3')),
                ('pan_no', models.CharField(blank=True, max_length=10, null=True)),
                ('caste', models.FileField(blank=True, upload_to='d/3')),
                ('income', models.FileField(blank=True, upload_to='d/4')),
                ('charactor_certificate', models.FileField(blank=True, upload_to='d/5')),
                ('mark10', models.FileField(blank=True, upload_to='d/6')),
                ('mark12', models.FileField(blank=True, upload_to='d/7')),
                ('mark_graduation', models.FileField(blank=True, upload_to='d/7')),
            ],
        ),
    ]
