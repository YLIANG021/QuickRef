"""Operators and UI list for camera background images."""

import os

import bpy
from bpy.props import CollectionProperty, StringProperty
from bpy.types import Operator, OperatorFileListElement, Panel, UIList

from .. import i18n
from ..core.reference_state import get_active_camera_bg, get_camera_and_settings, sync_ui_alpha_from_active


def poll_camera(cls, context):
    cam, _ = get_camera_and_settings(context)
    if cam is not None:
        return True
    cls.poll_message_set(i18n.tr_iface("No active camera"))
    return False


def poll_active_background(cls, context):
    if get_active_camera_bg(context)[2] is not None:
        return True
    cls.poll_message_set(i18n.tr_iface("No active reference image"))
    return False


class BG_OT_ToggleEnable(Operator):
    bl_idname = "quickref.toggle_visibility"
    bl_label = "Toggle Reference Visibility"
    bl_description = "Show or hide the active camera's reference images"
    bl_translation_context = i18n.CONTEXT
    bl_options = {'UNDO'}

    @classmethod
    def poll(cls, context):
        return poll_active_background(cls, context)

    def execute(self, context):
        context.scene.bg_opacity_settings.enable_control = not context.scene.bg_opacity_settings.enable_control
        return {'FINISHED'}


class BG_OT_ToggleDepth(Operator):
    bl_idname = "quickref.toggle_depth"
    bl_label = "Toggle Reference Layer"
    bl_description = "Display the active reference in front of or behind scene geometry"
    bl_translation_context = i18n.CONTEXT
    bl_options = {'UNDO'}

    @classmethod
    def poll(cls, context):
        return poll_active_background(cls, context)

    def execute(self, context):
        active_bg = get_active_camera_bg(context)[2]
        if active_bg:
            active_bg.display_depth = 'BACK' if active_bg.display_depth == 'FRONT' else 'FRONT'
        return {'FINISHED'}


class BG_OT_AddImage(Operator):
    bl_idname = "quickref.add_reference"
    bl_label = "Add Reference Image"
    bl_description = "Load one or more images as camera references"
    bl_translation_context = i18n.CONTEXT
    bl_options = {'UNDO'}

    filepath: StringProperty(name="Image File", translation_context=i18n.CONTEXT, subtype='FILE_PATH')
    directory: StringProperty(subtype='DIR_PATH')
    files: CollectionProperty(type=OperatorFileListElement)
    filter_glob: StringProperty(
        default="*.png;*.jpg;*.jpeg;*.tif;*.tiff;*.bmp;*.exr;*.hdr;*.tga",
        options={'HIDDEN'},
    )

    @classmethod
    def poll(cls, context):
        return poll_camera(cls, context)

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        paths = []
        if self.files:
            for f in self.files:
                paths.append(os.path.join(self.directory, f.name))
        elif self.filepath:
            paths.append(self.filepath)

        if not paths:
            return {'CANCELLED'}

        cam, settings = get_camera_and_settings(context)
        if not cam:
            return {'CANCELLED'}

        bg_images = cam.data.background_images
        template_alpha = settings.active_alpha

        new_indices = []
        for path in paths:
            try:
                image = bpy.data.images.load(path, check_existing=True)
            except Exception as e:
                details = f"{path} ({e})"
                self.report(
                    {'WARNING'},
                    i18n.tr_report("Failed to load image: {details}", details=details),
                )
                continue
            new_bg = bg_images.new()
            new_bg.image = image
            new_bg.alpha = template_alpha
            new_bg.display_depth = 'FRONT'
            new_bg.frame_method = 'FIT'
            new_bg.show_background_image = False
            new_indices.append(len(bg_images) - 1)

        if not new_indices:
            return {'CANCELLED'}

        settings.active_image_index = new_indices[-1]
        if settings.enable_control:
            cam.data.show_background_images = True
        sync_ui_alpha_from_active(settings, context=context)
        return {'FINISHED'}


class BG_OT_RemoveImage(Operator):
    bl_idname = "quickref.remove_reference"
    bl_label = "Remove Reference Image"
    bl_description = "Remove the active reference from the camera"
    bl_translation_context = i18n.CONTEXT
    bl_options = {'UNDO'}

    @classmethod
    def poll(cls, context):
        return poll_active_background(cls, context)

    def execute(self, context):
        cam, settings = get_camera_and_settings(context)
        if not cam:
            return {'CANCELLED'}
        bg_images = cam.data.background_images
        total = len(bg_images)
        if total == 0:
            return {'CANCELLED'}

        old_index = min(settings.active_image_index, total - 1)
        bg_images.remove(bg_images[old_index])

        new_total = len(bg_images)
        if new_total == 0:
            settings.active_image_index = 0
            return {'FINISHED'}

        new_index = min(old_index, new_total - 1)
        settings.active_image_index = new_index
        for i, bg in enumerate(bg_images):
            bg.show_background_image = (i == new_index)
        sync_ui_alpha_from_active(settings, context=context)
        return {'FINISHED'}


class BG_OT_ReplaceImage(Operator):
    bl_idname = "quickref.replace_reference"
    bl_label = "Replace Reference Image"
    bl_description = "Replace the image and keep its settings."
    bl_translation_context = i18n.CONTEXT
    bl_options = {'UNDO'}

    filepath: StringProperty(name="Image File", translation_context=i18n.CONTEXT, subtype='FILE_PATH')
    filter_glob: StringProperty(
        default="*.png;*.jpg;*.jpeg;*.tif;*.tiff;*.bmp;*.exr;*.hdr;*.tga",
        options={'HIDDEN'},
    )

    @classmethod
    def poll(cls, context):
        return poll_active_background(cls, context)

    def invoke(self, context, event):
        active_bg = get_active_camera_bg(context)[2]
        current_image = getattr(active_bg, "image", None) if active_bg else None
        if current_image and current_image.filepath:
            self.filepath = bpy.path.abspath(current_image.filepath)
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        active_bg = get_active_camera_bg(context)[2]
        if active_bg is None or not self.filepath:
            return {'CANCELLED'}

        try:
            image = bpy.data.images.load(self.filepath, check_existing=True)
        except Exception as exc:
            self.report(
                {'WARNING'},
                i18n.tr_report("Failed to load image: {details}", details=exc),
            )
            return {'CANCELLED'}

        active_bg.source = 'IMAGE'
        active_bg.image = image
        self.report(
            {'INFO'},
            i18n.tr_report("Reference image replaced: {name}", name=image.name),
        )
        return {'FINISHED'}


class BG_OT_DuplicateReference(Operator):
    bl_idname = "quickref.duplicate_reference"
    bl_label = "Duplicate Reference"
    bl_description = "Duplicate the image with independent settings."
    bl_translation_context = i18n.CONTEXT
    bl_options = {'UNDO'}

    @classmethod
    def poll(cls, context):
        return poll_active_background(cls, context)

    def execute(self, context):
        cam, settings, source_bg = get_active_camera_bg(context)
        if cam is None or settings is None or source_bg is None:
            return {'CANCELLED'}

        duplicate = cam.data.background_images.new()
        duplicate.source = source_bg.source
        if source_bg.source == 'IMAGE':
            duplicate.image = source_bg.image
        else:
            duplicate.clip = source_bg.clip

        duplicate.offset = source_bg.offset[:]
        duplicate.scale = source_bg.scale
        duplicate.rotation = source_bg.rotation
        duplicate.use_flip_x = source_bg.use_flip_x
        duplicate.use_flip_y = source_bg.use_flip_y
        duplicate.alpha = source_bg.alpha
        duplicate.use_camera_clip = source_bg.use_camera_clip
        duplicate.show_on_foreground = source_bg.show_on_foreground
        duplicate.display_depth = source_bg.display_depth
        duplicate.frame_method = source_bg.frame_method
        duplicate.show_background_image = False

        settings.active_image_index = len(cam.data.background_images) - 1
        if settings.enable_control:
            cam.data.show_background_images = True
        sync_ui_alpha_from_active(settings, context=context)
        return {'FINISHED'}


class BG_PT_ImageSettingsPopover(Panel):
    bl_idname = "BG_PT_image_settings_popover"
    bl_label = "Reference Image Settings"
    bl_translation_context = i18n.CONTEXT
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'

    @classmethod
    def poll(cls, context):
        return get_active_camera_bg(context)[2] is not None

    def draw(self, context):
        layout = self.layout
        if get_active_camera_bg(context)[2] is None:
            layout.label(
                text="No active reference image",
                text_ctxt=i18n.CONTEXT,
                icon='KEYTYPE_BREAKDOWN_VEC',
            )
            return

        reference_actions = layout.column(align=True)
        reference_actions.operator(BG_OT_ReplaceImage.bl_idname, icon='FILEBROWSER')
        reference_actions.operator(BG_OT_DuplicateReference.bl_idname, icon='DUPLICATE')


class BG_UL_BackgroundImages(UIList):
    bl_translation_context = i18n.CONTEXT

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        bg = item
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            if bg.image:
                layout.prop(bg.image, "name", text="", emboss=False, icon='IMAGE_DATA')
            else:
                layout.label(
                    text="(No Reference Image)",
                    text_ctxt=i18n.CONTEXT,
                    icon='FILE_IMAGE',
                )
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon='IMAGE_DATA' if bg.image else 'FILE_IMAGE')


CLASSES = (
    BG_OT_ToggleEnable,
    BG_OT_ToggleDepth,
    BG_OT_AddImage,
    BG_OT_RemoveImage,
    BG_OT_ReplaceImage,
    BG_OT_DuplicateReference,
    BG_PT_ImageSettingsPopover,
    BG_UL_BackgroundImages,
)
