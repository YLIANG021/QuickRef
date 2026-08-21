"""UI panels."""
from .header import (
    BG_PT_HeaderOpacitySettingsPopover,
    register_header,
    unregister_header,
)
from .panel_main import IMAGE_SWITCHER_PT_Panel

CLASSES = (
    BG_PT_HeaderOpacitySettingsPopover,
    IMAGE_SWITCHER_PT_Panel,
)

def register_panel_icons():
    """Compatibility hook retained for the lifecycle registry."""
    return None


def unregister_panel_icons():
    """Compatibility hook retained for the lifecycle registry."""
    return None

__all__ = (
    "CLASSES",
    "BG_PT_HeaderOpacitySettingsPopover",
    "IMAGE_SWITCHER_PT_Panel",
    "register_header",
    "register_panel_icons",
    "unregister_header",
    "unregister_panel_icons",
)
