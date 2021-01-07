# Generated by Django 3.0.6 on 2021-01-05 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='srs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('childs_age_month', models.IntegerField()),
                ('childs_age_year', models.IntegerField()),
                ('raters_name', models.CharField(max_length=250)),
                ('date_of_rating', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('staff', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='t_score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Awr', models.IntegerField()),
                ('Cog', models.IntegerField()),
                ('Com', models.IntegerField()),
                ('Mot', models.IntegerField()),
                ('RRB', models.IntegerField()),
                ('total_t_score', models.IntegerField(default=0, help_text="Don't insert any value")),
                ('childs_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profileSheet.srs')),
            ],
        ),
        migrations.AddField(
            model_name='srs',
            name='childs_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profileSheet.students'),
        ),
        migrations.CreateModel(
            name='raw_score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Awr', models.IntegerField()),
                ('Cog', models.IntegerField()),
                ('Com', models.IntegerField()),
                ('Mot', models.IntegerField()),
                ('RRB', models.IntegerField()),
                ('total_raw_score', models.IntegerField(default=0, help_text="Don't insert any value")),
                ('childs_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profileSheet.srs')),
            ],
        ),
    ]