# Generated by Django 2.2.3 on 2019-07-15 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('po', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pohead',
            name='po_no',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]