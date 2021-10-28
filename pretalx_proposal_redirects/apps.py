from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class PluginApp(AppConfig):
    name = "pretalx_proposal_redirects"
    verbose_name = "Proposal redirects"

    class PretalxPluginMeta:
        name = gettext_lazy("Proposal redirects")
        author = "Tobias Kunze"
        description = gettext_lazy("Redirects from pretalx.domain/shortcode to the matching proposal, if possible.")
        visible = True
        version = "0.0.0"

    def ready(self):
        from . import signals  # NOQA
