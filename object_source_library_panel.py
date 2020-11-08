# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_mesh_source

from bpy.types import Panel, UIList
from bpy.utils import register_class, unregister_class


class OBJECT_SOURCE_LIB_PT_panel_3d_view(Panel):
    bl_idname = 'OBJECT_SOURCE_LIB_PT_panel_3d_view'
    bl_label = 'Mesh Source Library'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Mesh Source'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.template_list(
            listtype_name='OBJECT_SOURCE_LIB_UL_lib_items',
            list_id='object_source_lib_items',
            dataptr=context.window_manager,
            propname='object_source_lib_items',
            active_dataptr=context.window_manager,
            active_propname='object_source_lib_active_item'
        )
        col = row.column(align=True)
        col.operator('object_source_lib.remove_item', icon='REMOVE', text='')


class OBJECT_SOURCE_LIB_UL_lib_items(UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_property, index=0, flt_flag=0):
        op = layout.operator('object_source_lib.item_from_library', icon='PLUGIN', text='')
        op.item_id = index
        layout.label(text=item.name)
        layout.label(text='', icon='MESH_CUBE')


def register():
    register_class(OBJECT_SOURCE_LIB_UL_lib_items)
    register_class(OBJECT_SOURCE_LIB_PT_panel_3d_view)


def unregister():
    unregister_class(OBJECT_SOURCE_LIB_PT_panel_3d_view)
    unregister_class(OBJECT_SOURCE_LIB_UL_lib_items)
