"""Ensure numbers module (defining <user.number_small> and related captures) is imported early.

This file is named with a leading "00_" so that Talon loads it before any
.talon files that reference <user.number_small>. All it does is import the
existing implementation so the captures and lists are registered early.
"""

from importlib import import_module

# Importing the numbers module registers the required lists/captures.
# import_module("user.talonconfig.core.numbers.numbers") 