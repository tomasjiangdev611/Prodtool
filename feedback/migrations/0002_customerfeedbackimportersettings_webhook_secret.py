# Generated by Django 2.1.3 on 2018-11-17 03:03

from django.db import migrations, models
import django.utils.timezone
import uuid

def set_webhook_secret_defaults(apps, schema_editor):
    CustomerFeedbackImporterSettings = apps.get_model('feedback', 'CustomerFeedbackImporterSettings')
    for cfis in CustomerFeedbackImporterSettings.objects.all():
        cfis.webhook_secret = str(uuid.uuid1())
        cfis.save()

class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerfeedbackimportersettings',
            name='webhook_secret',
            field=models.CharField(null=True, max_length=36),
        ),
        migrations.RunPython(set_webhook_secret_defaults),
        migrations.AlterField(
            model_name='customerfeedbackimportersettings',
            name='webhook_secret',
            field=models.CharField(max_length=36, unique=True),
        ),
    ]