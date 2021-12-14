from django.http import Http404
from django.shortcuts import redirect
from django_scopes import scopes_disabled
from pretalx.submission.models import Submission


def redirect_view(request, code):
    """Possible TODOs:

    - filter applicable events by domain
    - add a similar view for /orga urls
    """
    with scopes_disabled():
        submissions = Submission.objects.filter(code__iexact=code)
        if submissions.count() == 1:
            return redirect(submissions.first().urls.public.full())
        raise Http404
