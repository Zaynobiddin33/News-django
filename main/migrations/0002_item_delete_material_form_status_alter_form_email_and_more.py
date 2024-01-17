# Generated by Django 5.0.1 on 2024-01-17 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='items/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.region')),
            ],
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.AddField(
            model_name='form',
            name='status',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='form',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='form',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]