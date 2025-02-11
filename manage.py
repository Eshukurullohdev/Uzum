#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


from decouple import config

API_KEY = config('dcc7509b1aaaf08bf495f03bd9c8f9f2-449022bd-3b9f-48a1-82d0-0e7d306288e2', default='dcc7509b1aaaf08bf495f03bd9c8f9f2-449022bd-3b9f-48a1-82d0-0e7d306288e2')
