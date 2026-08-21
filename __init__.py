# SPDX-License-Identifier: GPL-3.0-or-later

"""QuickRef extension entry point."""

from .core.lifecycle import register, unregister

__all__ = (
    "register",
    "unregister",
)
