# Generated by Django 4.0.8 on 2024-04-19 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_alter_course_code_alter_course_credit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('Shanghai Port', 'Shanghai Port'), ('Port of Singapore', 'Port of Singapore'), ('Port of Rotterdam', 'Port of Rotterdam'), ('Port of Hong Kong', 'Port of Hong Kong'), ('Port of Busan', 'Port of Busan'), ('Port of Antwerp', 'Port of Antwerp'), ('Port of Hamburg', 'Port of Hamburg'), ('Port of Los Angeles', 'Port of Los Angeles'), ('Port of Long Beach', 'Port of Long Beach'), ('Port of Dubai', 'Port of Dubai')], max_length=200),
        ),
    ]
