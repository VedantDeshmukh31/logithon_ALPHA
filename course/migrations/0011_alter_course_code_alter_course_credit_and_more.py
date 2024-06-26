# Generated by Django 4.0.8 on 2024-04-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_remove_course_order_weight_remove_course_pincode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='credit',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='summary',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
