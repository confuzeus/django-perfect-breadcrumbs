def breadcrumbs(request):
    if hasattr(request, "breadcrumbs"):
        return {"breadcrumbs": request.breadcrumbs}
    return {}
