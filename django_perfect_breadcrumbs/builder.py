class Breadcrumb:
    def __init__(self, name, url=None, active=False):
        if url and active:
            raise ValueError("Active items can't have an url.")

        if url is None and not active:
            raise ValueError("Non-active items must have an url.")
        self.name = name
        self.url = url
        self.active = active


class BreadcrumbBuilder:
    def __init__(self, initial=None):
        if initial is None:
            initial = []
        else:
            if not isinstance(initial, list):
                raise ValueError("The initial object must be a list.")
            for item in initial:
                if not isinstance(item, Breadcrumb):
                    raise ValueError("Items must be Breadcrumb objects.")
        self.breadcrumbs = initial

    def add(self, name, url=None, active=False):
        self.breadcrumbs.append(Breadcrumb(name, url, active))

    def add_breadcrumb(self, breadcrumb):
        if not isinstance(breadcrumb, Breadcrumb):
            raise ValueError("The breadcrumb must be an uinst")
        self.breadcrumbs.append(breadcrumb)

    def add_bulk(self, breadcrumbs):
        if not isinstance(breadcrumbs, list):
            raise ValueError("breadcrumbs must be a list.")
        for breadcrumb in breadcrumbs:
            if isinstance(breadcrumb, dict):
                self.breadcrumbs.append(
                    Breadcrumb(
                        breadcrumb["name"],
                        breadcrumb.get("url", None),
                        breadcrumb.get("active", False),
                    )
                )
            elif isinstance(breadcrumb, Breadcrumb):
                self.breadcrumbs.append(breadcrumb)
            else:
                raise ValueError(
                    "A breadcrumb item must be either and instance of Breadcrumb or "
                    "dict."
                )
