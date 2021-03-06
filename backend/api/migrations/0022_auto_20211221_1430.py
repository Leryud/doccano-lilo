# Generated by Django 3.2.8 on 2021-12-21 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20211221_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='new_label',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.categorytype'),
        ),
        migrations.AddField(
            model_name='span',
            name='new_label',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.spantype'),
        ),
        migrations.AlterField(
            model_name='category',
            name='label',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.label'),
        ),
        migrations.AlterField(
            model_name='span',
            name='label',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.label'),
        ),
    ]
