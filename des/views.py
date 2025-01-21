from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.template import loader
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_http_methods

from des.helpers import get_configuration_admin_url
from des.models import DynamicEmailConfiguration

subject = getattr(settings, "DES_TEST_SUBJECT", _("Test Email"))
text_template = getattr(settings, "DES_TEST_TEXT_TEMPLATE", "des/test_email.txt")
html_template = getattr(settings, "DES_TEST_HTML_TEMPLATE", None)

message_text = loader.render_to_string(text_template)
message_html = loader.render_to_string(html_template) if html_template else None


@require_http_methods(["POST"])
def send_test_email(request):

    if request.user is None or not request.user.is_staff:
        return HttpResponseNotFound()

    email = request.POST.get("email", None)
    config = DynamicEmailConfiguration.get_solo()

    if email:
        try:
            send_mail(
                subject,
                message_text,
                config.from_email or None,
                [email],
                html_message=message_html,
            )

            messages.success(
                request,
                _(
                    'Test email sent. Please check "{}" for a '
                    'message with the subject "{}"'
                ).format(email, subject),
            )
        except Exception as e:
            messages.error(request, _("Could not send email. {}").format(e))
    else:
        messages.error(request, _("You must provide an email address to test with."))

    return HttpResponseRedirect(get_configuration_admin_url())


__all__ = ["send_test_email"]
