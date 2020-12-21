from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agen', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created',)},
        ),
    ]