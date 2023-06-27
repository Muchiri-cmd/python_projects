#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
=======
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")
>>>>>>> feea372ff8d2b558b178edc6f857898fb38b1e6f
>>>>>>> aecf3b8f20cf3b4e6b08ba79e5e6ac054ba1aace
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
