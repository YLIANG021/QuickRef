"""Helpers for entering the active camera view."""

import bpy


def _get_window_region(area):
    return next((region for region in area.regions if region.type == 'WINDOW'), None)


def show_camera_in_current_view(context, camera):
    area = getattr(context, "area", None)
    if area is None or area.type != 'VIEW_3D':
        return

    space = getattr(context, "space_data", None) or area.spaces.active
    region_3d = getattr(space, "region_3d", None)
    window_region = _get_window_region(area)
    if region_3d is None or window_region is None:
        return

    space.camera = camera
    if region_3d.view_perspective == 'CAMERA':
        area.tag_redraw()
        return

    smooth_view = context.preferences.view.smooth_view
    try:
        context.preferences.view.smooth_view = 0
        with context.temp_override(
            window=context.window,
            area=area,
            region=window_region,
            space_data=space,
        ):
            bpy.ops.view3d.view_camera()
    finally:
        context.preferences.view.smooth_view = smooth_view
