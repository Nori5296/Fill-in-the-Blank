# Generated by Django 2.0.9 on 2018-12-22 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FillquestionDetail',
            fields=[
                ('fillquestion_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=255)),
                ('answer_text', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'fillquestion_detail',
            },
        ),
        migrations.CreateModel(
            name='Fillquestions',
            fields=[
                ('fillquestion_id', models.AutoField(primary_key=True, serialize=False)),
                ('fillquestion_name', models.CharField(max_length=255)),
                ('registed_on', models.DateTimeField()),
                ('regist_user', models.IntegerField()),
                ('updated_on', models.DateTimeField()),
                ('update_user', models.IntegerField()),
            ],
            options={
                'db_table': 'fillquestions',
            },
        ),
        migrations.CreateModel(
            name='OriginalTexts',
            fields=[
                ('original_text_id', models.AutoField(primary_key=True, serialize=False)),
                ('original_text', models.TextField()),
                ('registed_on', models.DateTimeField()),
                ('regist_user', models.IntegerField()),
                ('updated_on', models.DateTimeField()),
                ('update_user', models.IntegerField()),
            ],
            options={
                'db_table': 'original_texts',
            },
        ),
        migrations.AddField(
            model_name='fillquestions',
            name='original_text',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='anaumeapp.OriginalTexts'),
        ),
        migrations.AddField(
            model_name='fillquestiondetail',
            name='fillquestion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='anaumeapp.Fillquestions'),
        ),
    ]