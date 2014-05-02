#!/usr/bin/env python
import os
import sys

"""
    ./menage.py makemessages --all
        After setting LOCALE_PATHS, in settings.py, this command
        generates one django.po for each language in the locale path.
"""

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "acidentes_em_rodovias.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
