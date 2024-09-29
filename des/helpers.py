from des.models import DynamicEmailConfiguration

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


def get_configuration_admin_url():
    meta = DynamicEmailConfiguration._meta
    return reverse("admin:{}_{}_change".format(meta.app_label, meta.model_name))


__all__ = ["get_configuration_admin_url"]
