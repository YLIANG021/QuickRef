"""3D View header controls."""

import bpy
from bpy.types import Panel

from .. import i18n
from ..core.reference_state import get_active_camera_bg
from ..features.background_images import BG_OT_ToggleEnable


def is_header_mode_allowed(context):
    mode = getattr(context, "mode", "")
    return mode == 'OBJECT' or mode == 'SCULPT' or mode.startswith('EDIT_')


def draw_header_opacity_controls(self, context):
    scene = getattr(context, "scene", None)
    settings = getattr(scene, "bg_opacity_settings", None)
    if not settings or not settings.show_header_controls:
        return
    if not is_header_mode_allowed(context):
        return

    _, _, active_bg = get_active_camera_bg(context)
    source = (
        getattr(active_bg, "image", None) or getattr(active_bg, "clip", None)
        if active_bg is not None
        else None
    )
    if source is None:
        return

    control_row = self.layout.row(align=True)
    if settings.show_header_visibility_toggle:
        control_row.operator(
            BG_OT_ToggleEnable.bl_idname,
            text="",
            icon='OUTLINER_OB_IMAGE' if settings.enable_control else 'PANEL_CLOSE',
            depress=settings.enable_control,
        )

    slider_row = control_row.row(align=True)
    slider_row.ui_units_x = settings.header_opacity_width
    if settings.enable_control:
        slider_row.prop(settings, "active_alpha", text="", slider=True)
    else:
        slider_row.enabled = False
        slider_row.prop(settings, "stored_opacity", text="", slider=True)


class BG_PT_HeaderOpacitySettingsPopover(Panel):
    bl_idname = "BG_PT_header_opacity_settings_popover"
    bl_label = "Header Opacity"
    bl_translation_context = i18n.CONTEXT
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'

    def draw(self, context):
        settings = context.scene.bg_opacity_settings
        layout = self.layout
        layout.prop(
            settings,
            "header_opacity_width",
            text="Slider Width",
            text_ctxt=i18n.CONTEXT,
        )
        layout.prop(
            settings,
            "show_header_visibility_toggle",
            text="Quick Background Toggle",
            text_ctxt=i18n.CONTEXT,
        )


def register_header():
    bpy.types.VIEW3D_HT_header.append(draw_header_opacity_controls)


def unregister_header():
    bpy.types.VIEW3D_HT_header.remove(draw_header_opacity_controls)
