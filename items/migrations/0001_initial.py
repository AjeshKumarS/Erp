# Generated by Django 2.2.3 on 2019-07-15 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uom', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_code', models.IntegerField(primary_key=True, serialize=False)),
                ('item_desc', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('uom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Uom')),
            ],
        ),
    ]
