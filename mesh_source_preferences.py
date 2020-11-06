# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_mesh_source

from bpy.types import AddonPreferences
from bpy.props import StringProperty
from bpy.utils import register_class, unregister_class


class MESH_SOURCE_preferences(AddonPreferences):
    bl_idname = __package__

    export_path: StringProperty(
        name='Export Path',
        subtype='DIR_PATH',
        default=''
    )

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.label(text='Export')
        box.prop(self, property='export_path')


def register():
    register_class(MESH_SOURCE_preferences)


def unregister():
    unregister_class(MESH_SOURCE_preferences)
