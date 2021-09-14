# Generated by Django 3.2.6 on 2021-09-08 15:12

from django.db import migrations, models

import authentik.lib.utils.time


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_providers_oauth2", "0016_alter_authorizationcode_nonce"),
    ]

    operations = [
        migrations.AlterField(
            model_name="oauth2provider",
            name="token_validity",
            field=models.TextField(
                default="days=30",
                help_text="Tokens not valid on or after current time + this value (Format: hours=1;minutes=2;seconds=3).",
                validators=[authentik.lib.utils.time.timedelta_string_validator],
            ),
        ),
    ]