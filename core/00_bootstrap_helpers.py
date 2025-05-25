from __future__ import annotations
"""Bootstrap helper utilities.

This file is imported by Talon very early in the user load sequence because the
filename begins with ``00_`` (which sorts before the rest of our modules).  Its
sole purpose is to guarantee that helper modules which declare actions/settings
used elsewhere are imported *before* any other user modules attempt to call
those actions.

Notably, some modules such as ``core.app_switcher`` and ``core.system_paths``
rely on the actions provided by :pymod:`core.create_spoken_forms` and
:pyfile:`backup_community/plugin/talon_helpers/talon_helpers.py` respectively.
If those helpers have not yet been loaded then Talon raises a ``KeyError`` such
as::

    KeyError: "Action 'user.create_spoken_forms_from_list' is not declared."

or::

    KeyError: "Action 'user.talon_get_active_registry_list' is not declared."

Importing the helper modules here eliminates those race-conditions.
"""

# Importing with the fully-qualified package path ensures Talon registers the
# actions contained in these modules.  We wrap each import in a ``try`` block so
# Talon will still start even if a module is missing.

try:
    import user.core.create_spoken_forms  # noqa: F401 – registers create_spoken_forms actions
except Exception as e:  # pragma: no cover – we only log, not raise
    from talon import app

    app.logger.warning(
        f"[bootstrap] Failed to import user.core.create_spoken_forms: {e}"
    )

try:
    # Provides talon_get_* helper actions that other modules depend on.
    import user.plugin.talon_helpers.talon_helpers  # noqa: F401
except Exception:
    # Fall back to legacy path used before the plugin was moved.
    try:
        import user.backup_community.plugin.talon_helpers.talon_helpers  # noqa: F401
    except Exception as e:  # pragma: no cover – we only log, not raise
        from talon import app

        app.logger.warning(
            f"[bootstrap] Failed to import talon_helpers module: {e}"
        ) 