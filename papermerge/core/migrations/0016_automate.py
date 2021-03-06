# Generated by Django 3.0.7 on 2020-07-21 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200615_0525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('match', models.CharField(blank=True, max_length=256)),
                ('matching_algorithm', models.PositiveIntegerField(choices=[(1, 'Any'), (2, 'All'), (3, 'Literal'), (4, 'Regular Expression')], default=1)),
                ('is_case_sensitive', models.BooleanField(default=True)),
                ('plugin_name', models.CharField(blank=True, max_length=256)),
                ('extract_page', models.BooleanField(default=False)),
                ('dst_folder', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Folder')),
            ],
        ),
    ]
