# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_mesh_source

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class MESH_SOURCE_PT_panel_3d_view(Panel):
    bl_idname = 'MESH_SOURCE_PT_panel_3d_view'
    bl_label = 'Mesh Source Builder'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Mesh Source'

    def draw(self, context):
        layout = self.layout
        layout.operator('mesh_source.mesh_to_text', icon='MESH_DATA')
        layout.operator('mesh_source.mesh_to_library', icon='PACKAGE')
        box = layout.box()
        box.label(text='Export')
        box.operator('mesh_source.library_to_add_on', icon='SETTINGS')
        box.prop(data=context.preferences.addons[__package__].preferences, property='export_path')


def register():
    register_class(MESH_SOURCE_PT_panel_3d_view)


def unregister():
    unregister_class(MESH_SOURCE_PT_panel_3d_view)
