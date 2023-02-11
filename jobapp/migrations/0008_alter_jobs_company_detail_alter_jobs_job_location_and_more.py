# Generated by Django 4.1.2 on 2022-11-16 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0007_remove_jobs_qualification_text_jobs_responsibility1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='company_detail',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='job_location',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='qualification1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='qualification2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='qualification3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='qualification4',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='responsibility1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='responsibility2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='responsibility3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='responsibility4',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]