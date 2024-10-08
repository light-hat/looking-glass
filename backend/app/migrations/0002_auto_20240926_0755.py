# Generated by Django 3.2.25 on 2024-09-26 07:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=600)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Кейс',
                'verbose_name_plural': 'Кейсы',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CompromiseIndicator',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('elastic_id', models.CharField(max_length=600)),
                ('description', models.TextField()),
                ('mitre_tags', models.CharField(max_length=600)),
            ],
            options={
                'verbose_name': 'IoC',
                'verbose_name_plural': "IoC's",
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CyberAttack',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('attacker', models.CharField(blank=True, max_length=600, null=True)),
                ('victim', models.CharField(max_length=600)),
                ('attack_type', models.CharField(max_length=600)),
                ('success', models.BooleanField(default=False)),
                ('justification', models.TextField()),
                ('killchain_phase', models.CharField(choices=[('reconnaissance', 'Reconnaissance'), ('weaponization', 'Weaponization'), ('delivery', 'Delivery'), ('exploitation', 'Exploitation'), ('installation', 'Installation'), ('command_and_control', 'Command and Control'), ('actions_on_objectives', 'Actions on Objectives')], max_length=50)),
            ],
            options={
                'verbose_name': 'Атака',
                'verbose_name_plural': 'Атаки',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('host', models.CharField(max_length=600)),
            ],
            options={
                'verbose_name': 'Устройство',
                'verbose_name_plural': 'Устройства',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='DeviceUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=600)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='app.device')),
            ],
            options={
                'verbose_name': 'Пользователь устройства',
                'verbose_name_plural': 'Пользователи устройств',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Dump',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('processing', 'В обработке'), ('ready', 'Готово'), ('error', 'Ошибка анализа')], max_length=50)),
                ('filename', models.CharField(max_length=600)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('dump_type', models.CharField(choices=[('disk', 'Disk Dump'), ('memory', 'Memory Dump'), ('traffic', 'Traffic Dump')], max_length=50)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dumps', to='app.case')),
            ],
            options={
                'verbose_name': 'Дамп',
                'verbose_name_plural': 'Дампы',
                'ordering': ['-id'],
            },
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
        migrations.AddField(
            model_name='device',
            name='dump',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='app.dump'),
        ),
        migrations.AddField(
            model_name='cyberattack',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cyberattacks', to='app.device'),
        ),
        migrations.AddField(
            model_name='cyberattack',
            name='users',
            field=models.ManyToManyField(related_name='cyberattacks', to='app.DeviceUser'),
        ),
    ]
