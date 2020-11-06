# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_mesh_source

import bpy
from bpy.props import IntProperty
from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from .object_source_library import ObjectSourceLibrary


class OBJECT_SOURCE_LIB_OT_item_from_library(Operator):
    bl_idname = 'object_source_lib.item_from_library'
    bl_label = 'Get item from Library'
    bl_description = 'Get item from Object Source library'
    bl_options = {'REGISTER', 'UNDO'}

    item_id: IntProperty(
        default=-0
    )

    def execute(self, context):
        # add item from source library to scene
        active_item_id = context.window_manager.object_source_lib_active_item
        if active_item_id != self.item_id:
            context.window_manager.object_source_lib_active_item = self.item_id
        alias = context.window_manager.object_source_lib_items[context.window_manager.object_source_lib_active_item].name
        ObjectSourceLibrary.item_from_library(
            context=context,
            alias=alias
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        if 0 <= context.window_manager.object_source_lib_active_item < len(context.window_manager.object_source_lib_items):
            return True
        else:
            return False


class OBJECT_SOURCE_LIB_OT_remove_item(Operator):
    bl_idname = 'object_source_lib.remove_item'
    bl_label = 'Remove item from Library'
    bl_description = 'Remove item from Object Source library'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ObjectSourceLibrary.remove_item_from_library(
            context=context,
            scene_data=bpy.data
        )
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=200)

    def draw(self, context):
        layout = self.layout
        layout.label(text='Removed item can not be restored!')
        layout.label(text='Are you sure?')

    @classmethod
    def poll(cls, context):
        if 0 <= context.window_manager.object_source_lib_active_item < len(context.window_manager.object_source_lib_items):
            return True
        else:
            return False


def register():
    register_class(OBJECT_SOURCE_LIB_OT_item_from_library)
    register_class(OBJECT_SOURCE_LIB_OT_remove_item)


def unregister():
    unregister_class(OBJECT_SOURCE_LIB_OT_remove_item)
    unregister_class(OBJECT_SOURCE_LIB_OT_item_from_library)
