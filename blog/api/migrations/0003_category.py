# Generated by Django 3.1.7 on 2022-05-17 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='api.post')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]
