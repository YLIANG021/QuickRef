"""Top-level add-on register/unregister orchestration."""

from bpy.props import PointerProperty
from bpy.types import Scene, WindowManager

from . import registry, subscriptions
from .. import i18n
from ..features import adjust
from ..properties.settings import BG_AdjustRuntimeSettings, BG_Opacity_Settings


def register():
    i18n.register()
    registry.ui.register_panel_icons()
    registry.register_classes()
    Scene.bg_opacity_settings = PointerProperty(type=BG_Opacity_Settings)
    WindowManager.quickref_runtime = PointerProperty(
        type=BG_AdjustRuntimeSettings,
    )
    registry.ui.register_header()
    subscriptions.register()


def unregister():
    adjust.stop_active_adjust()
    subscriptions.unregister()
    if hasattr(Scene, 'bg_opacity_settings'):
        del Scene.bg_opacity_settings
    if hasattr(WindowManager, 'quickref_runtime'):
        del WindowManager.quickref_runtime

    registry.ui.unregister_header()
    registry.unregister_classes()
    registry.ui.unregister_panel_icons()
    i18n.unregister()
