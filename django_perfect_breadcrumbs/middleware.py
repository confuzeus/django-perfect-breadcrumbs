import importlib

from . import settings

builder_module_name, builder_class_name = settings.PERFECT_BREADCRUMBS_BUILDER.rsplit(
    ".", 1
)
builder_module = importlib.import_module(builder_module_name)
builder_class = getattr(builder_module, builder_class_name)


class BreadcrumbsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        builder = builder_class()
        request.breadcrumb_builder = builder
        request.breadcrumbs = builder.breadcrumbs
        response = self.get_response(request)

        return response
