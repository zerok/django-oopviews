===============
django-oopviews
===============

.. contents::

Base-implementation
===================

In some instances you end up producing tons of views that actually do mostly
the same except for perhaps one or two lines. This module offers you a simple
alternative::
    
    from django_oopviews.base import create_view, BaseView
    
    class View1(BaseView):
        def __init__(self, request, \*args, \*\*kwargs):
            # Here you have your common code
            self.my_variable = 1
        def __call__(self, request, \*args, \*\*kwargs):
            whatever = self.my_variable + 1
            return HttpResponse(whatever)
    
    class View2(View1):
        def __call__(self, request, \*args, \*\*kwargs):
            return HttpResponse(self.my_variable)

    view1 = create_view(View1)
    view2 = create_view(View2)

In this example, the code in ``View1.__init__`` is shared between View1 and 
View2, so you don't need to write it again.

If you want to share some HttpResponse post-processing, implement the
``BaseView.__after__(self, response_obj)`` method

For more details check out this `blog post`_

.. _blog post: http://zerokspot.com/weblog/1037/

Addons
========

Content-Type-Negotitation with OOPViews
---------------------------------------

In some situations it comes in handy, to do some content type negotiation
to really provide an optimized view for the user depending on what a user's
application supports (say WML or HTML or XML over HTML). HTTP/1.1 handles
this using the "Accept"-request header to give the user the option, to say
what kind of content type she'd prefer or give a list of content types 
prioritized with a value between 0 and 1.

This abstract view class should demonstrate, how you can easily handle such
situations within Django purely in the view code. The idea is pretty simple:
Simply use the ``__call__`` method as dispatcher for content-type-specific
methods.

To use this code, simply inherit the basic implementation and then specify
your content-type-specific methods and register them in the 
``ctn_accept_binding``-dictionary::
    
    from django.http import HttpResponse
    from django_oopview import ctn

    class TestView(ctn.AbstractCTNView):
        ctn_accept_binding = {
            'text/html': 'html',
            'text/*': 'html',
            '*/*': 'html',
        }

        def html(self, request, *args, **kwargs):
            return HttpResponse("Hello", mimetype='text/html')

The ``ctn_accept_binding``-dictionary not only allows you to bind a method to a 
content-type, but if you set a value to a tuple instead of just a string, it
will take the first element of that tuple as a priority value similar to the
one used in the "Accept"-handling. This way, you can prioritize methods for 
the case, that the user requests any type of a given family like for instance
'text/\*'.
