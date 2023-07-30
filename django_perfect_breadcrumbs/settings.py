from django.conf import settings

if hasattr(settings, "PERFECT_BREADCRUMBS_BUILDER"):
    PERFECT_BREADCRUMBS_BUILDER = settings.PERFECT_BREADCRUMBS_BUILDER
else:
    PERFECT_BREADCRUMBS_BUILDER = "django_perfect_breadcrumbs.builder.BreadcrumbBuilder"
