# Perfect Breadcrumbs

Breadcrumbs for perfectionists with deadlines.

## About

This package provides an easy way to add breadcrumbs to your Django project.

## Usage

1. Install the package with pip or poetry like so:

```shell
poetry add django_perfect_breadcrumbs
```

2. Add the middleware to in your `settings.py`:

```python
MIDDLEWARE = [
    ...
    "django_perfect_breadcrumbs.middleware.BreadcrumbsMiddleware",
]
```

3. Add the context processor in your `settings.py`:

```python
TEMPLATES = [
    {
        ...
    "OPTIONS": {
    "context_processors": [
        ...
        "django_perfect_breadcrumbs.context_processors.breadcrumbs",
    ],
},
},
]
```

You will now have access to `breadcrumb_builder` and `breadcrumbs` in view
`request` objects.

Your templates will also contain the `breadcrumbs` variables.

## Builder

Use the builder to add your breadcrumbs:

```python
def home(request):
    return render(request, "testapp/index.html")


def about(request):
    request.breadcrumb_builder.add("Home", reverse_lazy("home"))
    request.breadcrumb_builder.add("About", active=True)
    return render(request, "testapp/about.html")


def about_josh(request):
    breadcrumbs = [
        {"name": "Home", "url": reverse_lazy("home")},
        {"name": "about", "url": reverse_lazy("about")},
        {"name": "About Josh", "active": True},
    ]
    request.breadcrumb_builder.add_bulk(breadcrumbs)
    return render(request, "testapp/josh.html")
```

Then use breadcrumbs in your templates:

```html

<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    {% for breadcrumb in breadcrumbs %}
    {% if breadcrumb.active %}
    <li class="breadcrumb-item active"
        aria-current="page">{{ breadcrumb.name }}
    </li>
    {% else %}
    <li class="breadcrumb-item"><a
        href="{{ breadcrumb.url }}">{{ breadcrumb.name }}</a></li>
    {% endif %}
    {% endfor %}
  </ol>
</nav>
```

## License

MIT
