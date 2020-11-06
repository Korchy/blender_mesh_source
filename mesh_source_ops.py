# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_mesh_source

import bpy
from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from .object_source import ObjectSource


class MESH_SOURCE_OT_mesh_to_text(Operator):
    bl_idname = 'mesh_source.mesh_to_text'
    bl_label = 'Mesh to Text'
    bl_description = 'Convert mesh to source'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ObjectSource.object_to_text(
            objects=context.selected_objects,
            context=context,
            scene_data=bpy.data
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        if context.selected_objects:
            return True
        else:
            return False


class MESH_SOURCE_OT_mesh_to_library(Operator):
    bl_idname = 'mesh_source.mesh_to_library'
    bl_label = 'Mesh to Library'
    bl_description = 'Add mesh to source library'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ObjectSource.object_to_library(
            objects=context.selected_objects,
            context=context,
            scene_data=bpy.data
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        if context.selected_objects:
            return True
        else:
            return False


class MESH_SOURCE_OT_library_to_add_on(Operator):
    bl_idname = 'mesh_source.library_to_add_on'
    bl_label = 'Distribute Library as Add-on'
    bl_description = 'Export Mesh Source library as separate add-on'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ObjectSource.library_to_add_on(
            context=context
        )
        return {'FINISHED'}


def register():
    register_class(MESH_SOURCE_OT_mesh_to_text)
    register_class(MESH_SOURCE_OT_mesh_to_library)
    register_class(MESH_SOURCE_OT_library_to_add_on)


def unregister():
    unregister_class(MESH_SOURCE_OT_library_to_add_on)
    unregister_class(MESH_SOURCE_OT_mesh_to_library)
    unregister_class(MESH_SOURCE_OT_mesh_to_text)
