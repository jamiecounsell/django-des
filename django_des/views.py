from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django_des.models import DynamicEmailConfiguration
from django.core.mail import send_mail
from django_des.models import DynamicEmailConfiguration


@require_http_methods(["POST"])
def send_test_email(request):
    email = request.POST.get('email', None)
    config = DynamicEmailConfiguration.get_solo()

    if email:
        try:
            send_mail("Test Email", "This is a test", config.email_from_email, [email])
            messages.success(request, "Test email sent. Please check \"{}\"".format(email))
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
