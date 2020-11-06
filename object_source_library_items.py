# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_mesh_source

import bpy
from bpy.props import CollectionProperty, StringProperty, IntProperty
from bpy.types import PropertyGroup, WindowManager
from bpy.utils import register_class, unregister_class
from .object_source_library import ObjectSourceLibrary


class OBJECT_SOURCE_lib_items(PropertyGroup):

    name: StringProperty()


def register():
    register_class(OBJECT_SOURCE_lib_items)
    WindowManager.object_source_lib_items = CollectionProperty(type=OBJECT_SOURCE_lib_items)
    WindowManager.object_source_lib_active_item = IntProperty(
        name='active item',
        default=0
    )
    ObjectSourceLibrary.init_library_items(context=bpy.context)


def unregister():
    ObjectSourceLibrary.clear_library_items(context=bpy.context)
    del WindowManager.object_source_lib_active_item
    del WindowManager.object_source_lib_items
    unregister_class(OBJECT_SOURCE_lib_items)
