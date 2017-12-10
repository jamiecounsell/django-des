from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.template import loader
from django.conf import settings
from django.core.mail import send_mail
from django_des.models import DynamicEmailConfiguration

subject = getattr(settings, 'DES_TEST_SUBJECT', "Test Email")
text_template = getattr(settings, 'DES_TEST_TEXT_TEMPLATE', "des/test_email.txt")
html_template = getattr(settings, 'DES_TEST_HTML_TEMPLATE', None)

message_text = loader.render_to_string(text_template)
message_html = loader.render_to_string(html_template) if html_template else None


@require_http_methods(["POST"])
def send_test_email(request):
    email = request.POST.get('email', None)
    config = DynamicEmailConfiguration.get_solo()

    if email:
        try:
            send_mail(
                subject,
                message_text,
                config.email_from_email,
                [email],
                html_message = message_html)

            messages.success(request,
                ("Test email sent. Please check \"{}\" for a "
                 "message with the subject \"{}\"").format(
                    email,
                    subject
                )
            )
        except Exception as e:
            messages.error(request, "Could not send email. {}".format(e))
    else:
        messages.error(request, "You must provide an email address to test with.")

    meta = DynamicEmailConfiguration._meta
    return HttpResponseRedirect(
        reverse('admin:{}_{}_change'.format(
            meta.app_label, meta.model_name
        ))
    )


__all__ = ['send_test_email']
