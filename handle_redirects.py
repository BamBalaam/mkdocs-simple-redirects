from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files

def on_files(files: Files, config: MkDocsConfig) -> Files:
    """Inject redirect HTML stubs into the file collection"""
    redirects = config.get("extra", {}).get("redirects", {})
    for old_path, new_path in redirects.items():
        if new_path.startswith("https://"):
            url = new_path
        else:
            old_depth = old_path.rstrip("/").count("/")
            prefix = "../" * (old_depth + 1)
            url = f"{prefix}{new_path}"
        html = """<meta http-equiv="refresh" content="0; URL={url}" />""".format(url=url)
        stub = File.generated(
            config,
            f"{old_path.rstrip('/')}/index.html",
            content=html,
        )
        files.append(stub)

    return files
