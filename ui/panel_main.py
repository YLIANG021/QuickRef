"""Main Reference Images panel."""

from bpy.types import Panel

from .. import i18n
from ..core.reference_state import get_active_camera_bg
from ..features import adjust
from ..features.background_images import (
    BG_OT_AddImage,
    BG_OT_RemoveImage,
    BG_OT_ToggleDepth,
    BG_OT_ToggleEnable,
    BG_PT_ImageSettingsPopover,
)
from .header import BG_PT_HeaderOpacitySettingsPopover


class IMAGE_SWITCHER_PT_Panel(Panel):
    bl_label = "QuickRef"
    bl_translation_context = i18n.CONTEXT
    bl_idname = "IMAGE_SWITCHER_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'View'
    bl_order = 5

    def draw(self, context):
        layout = self.layout
        cam, settings, active_bg = get_active_camera_bg(context)

        if not cam:
            layout.label(
                text="No active camera",
                text_ctxt=i18n.CONTEXT,
                icon='CAMERA_DATA',
            )
            return

        if not cam.data.background_images:
            add_reference_row = layout.row()
            add_reference_row.scale_y = 1.5
            add_reference_row.operator(
                BG_OT_AddImage.bl_idname,
                text="Add Reference Image",
                text_ctxt=i18n.CONTEXT,
                icon='ADD',
            )
            return

        row = layout.row(align=True)
        row.scale_y = 1.2
        button_split = row.split(factor=1 / 3, align=True)
        add_column = button_split.column(align=True)
        add_column.operator(
            BG_OT_AddImage.bl_idname,
            text="",
            text_ctxt=i18n.CONTEXT,
            icon='ADD',
        )
        remaining_split = button_split.column(align=True).split(factor=0.5, align=True)
        remove_column = remaining_split.column(align=True)
        remove_column.operator(
            BG_OT_RemoveImage.bl_idname,
            text="",
            text_ctxt=i18n.CONTEXT,
            icon='REMOVE',
        )

        runtime = adjust.get_adjust_runtime(context)
        is_running = bool(runtime and runtime.running)
        has_reference_image = bool(
            active_bg
            and (getattr(active_bg, "image", None) or getattr(active_bg, "clip", None))
        )
        adjust_button = remaining_split.column(align=True)
        adjust_button.enabled = has_reference_image
        adjust_button.operator(
            adjust.VIEW3D_OT_quickref_adjust_reference.bl_idname,
            text="Adjust",
            text_ctxt=i18n.CONTEXT,
            depress=is_running,
        )
        image_settings = row.row(align=True)
        image_settings.enabled = active_bg is not None
        image_settings.popover(
            panel=BG_PT_ImageSettingsPopover.bl_idname,
            text="",
            icon='PREFERENCES',
        )

        layout.template_list(
            "BG_UL_BackgroundImages",
            "",
            cam.data,
            "background_images",
            settings,
            "active_image_index",
            rows=4,
        )

        main_box = layout.box()
        is_controllable = bool(active_bg)

        control_row = main_box.row(align=True)
        control_row.scale_y = 1.2
        if not is_controllable:
            control_row.enabled = False

        control_row.operator(
            BG_OT_ToggleEnable.bl_idname,
            text="",
            icon='OUTLINER_OB_IMAGE' if settings.enable_control else 'PANEL_CLOSE',
            depress=settings.enable_control,
        )

        if settings.enable_control:
            control_row.prop(
                settings,
                "active_alpha",
                text="Opacity",
                text_ctxt=i18n.CONTEXT,
                slider=True,
            )
        else:
            disabled_row = control_row.row()
            disabled_row.enabled = False
            disabled_row.prop(
                settings,
                "stored_opacity",
                text="Opacity",
                text_ctxt=i18n.CONTEXT,
                slider=True,
            )

        if is_controllable and settings.enable_control:
            main_box.label(text="Image Layer", text_ctxt=i18n.CONTEXT)
            depth_row = main_box.row()
            depth_row.scale_y = 1.1
            depth_icon = 'SORT_ASC' if active_bg.display_depth == 'FRONT' else 'SORT_DESC'
            depth_text = "Front" if active_bg.display_depth == 'FRONT' else "Back"
            depth_row.operator(
                BG_OT_ToggleDepth.bl_idname,
                text=depth_text,
                text_ctxt=i18n.CONTEXT,
                icon=depth_icon,
            )

        layout.separator(factor=0.5)
        header_row = layout.row(align=True)
        header_row.prop(
            settings,
            "show_header_controls",
            text="Header Opacity",
            text_ctxt=i18n.CONTEXT,
            toggle=True,
        )
        header_settings = header_row.row(align=True)
        header_settings.enabled = settings.show_header_controls
        header_settings.popover(
            panel=BG_PT_HeaderOpacitySettingsPopover.bl_idname,
            text="",
            icon='PREFERENCES',
        )

CLASSES = (
    IMAGE_SWITCHER_PT_Panel,
)
