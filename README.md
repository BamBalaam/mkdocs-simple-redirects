# mkdocs-simple-redirects

Extremely simple Hook (MkDocs>=1.4) to insert redirect HTML stubs into your MkDocs project.

Works with both internal pages and external pages!

## Installation

Just add the `handle_redirects.py` file to your MkDocs hooks folder and load it into your `mkdocs.yml`:

```yml
hooks:
  (...)
  - path/to/hooks/handle_redirects.py
```

## And then what?

Then you can add a list of redirections into the `extras` section of your `mkdocs.yml`

```yml
extra:
  (...)
  redirects:
    old/internal/page/: new/existing/internal/page/
    other/old/internal/page/: https://www.some-external-page.com/
```
