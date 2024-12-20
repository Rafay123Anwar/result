# Generated by Django 5.1.3 on 2024-12-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=10, unique=True)),
                ('linear_algebra', models.CharField(max_length=2)),
                ('oop_theory', models.CharField(max_length=2)),
                ('oop_practical', models.CharField(max_length=2)),
                ('pakistan_studies', models.CharField(max_length=2)),
                ('islamic_studies', models.CharField(max_length=2)),
                ('digital_logic_theory', models.CharField(max_length=2)),
                ('digital_logic_practical', models.CharField(max_length=2)),
                ('communication_skills', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Result1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=10, unique=True)),
                ('applied_physics_theory', models.CharField(max_length=2)),
                ('applied_physics_practical', models.CharField(max_length=2)),
                ('calculus_and_analytical_geometry', models.CharField(max_length=2)),
                ('functional_english', models.CharField(max_length=2)),
                ('intro_to_info_and_comm_techns_theory', models.CharField(max_length=2)),
                ('intro_to_info_and_comm_techns_practical', models.CharField(max_length=2)),
                ('programming_fundamentals_theory', models.CharField(max_length=2)),
                ('programming_fundamentals_practical', models.CharField(max_length=2)),
            ],
        ),
    ]