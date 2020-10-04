# Generated by Django 3.1.2 on 2020-10-04 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('age', models.IntegerField()),
                ('adoption_date', models.DateField(auto_now_add=True)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('details', models.TextField(blank=True)),
                ('deleted', models.BooleanField(null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['adoption_date'],
            },
        ),
    ]
