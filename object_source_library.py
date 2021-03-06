# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_mesh_source

import os
import shutil


class ObjectSourceLibrary:

    idname = 'object_source_library'

    @classmethod
    def item_from_library(cls, context, alias):
        # get item from library
        source_file_path = os.path.join(cls.library_path(), alias + '.py')
        if os.path.exists(source_file_path):
            exec(compile(open(source_file_path).read(), source_file_path, 'exec'))

    @classmethod
    def remove_item_from_library(cls, context, scene_data):
        # remove item from library
        # remove files
        alias = context.window_manager.object_source_lib_items[context.window_manager.object_source_lib_active_item].name
        source_file_path = os.path.join(cls.library_path(), alias + '.py')
        source_file_ext_items_path = os.path.join(cls.library_path(), alias)
        if os.path.exists(source_file_path):
            os.remove(source_file_path)
        if os.path.exists(source_file_ext_items_path):
            shutil.rmtree(source_file_ext_items_path)
        # remove item from list
        context.window_manager.object_source_lib_items.remove(context.window_manager.object_source_lib_active_item)

    @staticmethod
    def clear_library_items(context):
        # clear items from library list
        context.window_manager.object_source_lib_items.clear()

    @classmethod
    def init_library_items(cls, context):
        # init items for library list
        (_, _, source_files) = next(os.walk(cls.library_path()))
        for source_file in source_files:
            lib_item = context.window_manager.object_source_lib_items.add()
            lib_item.name = os.path.splitext(source_file)[0]

    @classmethod
    def library_path(cls):
        # return path to material library sources
        library_path = os.path.join(os.path.dirname(__file__), cls.idname)
        if not os.path.exists(library_path):
            os.makedirs(library_path)
        return library_path
