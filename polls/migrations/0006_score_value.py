# Generated by Django 4.2.1 on 2023-05-31 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_score_score_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score_Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_value_text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.score')),
            ],
        ),
    ]
