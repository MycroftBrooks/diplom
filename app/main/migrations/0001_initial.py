# Generated by Django 4.2.2 on 2024-04-14 13:33

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
            name='Treaty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Дата создания договора')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Название договора')),
                ('number', models.FloatField(blank=True, null=True, verbose_name='Номер договора')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Дата первой подачи показания')),
                ('record', models.IntegerField(blank=True, null=True, verbose_name='Показание')),
                ('multiplier', models.FloatField(blank=True, null=True, verbose_name='Тариф')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения показания')),
                ('treaty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.treaty')),
            ],
        ),
    ]