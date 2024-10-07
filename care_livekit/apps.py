from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

PLUGIN_NAME = "care_livekit"


class LivekitConfig(AppConfig):
    name = PLUGIN_NAME
    verbose_name = _("Livekit")
