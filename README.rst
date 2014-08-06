=========================
django_bootstrap_carousel
=========================

django-bootstrap-carousel is a carousel component using Bootstrap 3 for Django.


Installation
============

You can using ``pip`` or ``easy_install`` to install `django-bootstrap-carousel` app.


Setup
=====

Add app to your Django ``settings.py``::

    INSTALLED_APPS = (
        # Other apps here.
        'django_bootstrap_carousel'
    )


Usage
=====

1. Create your carousel and carousel item in the Django admin app.

2. Get carouse object in your view and put it to the context::

    def my_view(request):
        ## Your code here.
        carousel = Carousel.objects.get(pk=1)
        return render_to_response(
            'my_view.html',
            {
                'carousel': carousel,
            },
            context_instance=RequestContext(request)
        )


3. In your template, load the ``bootstrap_carousel_tags`` template tags first::

    {% load bootstrap_carousel_tags %}


4. Using the ``render_carousel`` template tag, like::

    {% render_carousel carousel %}

