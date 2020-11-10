# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_mesh_source


import os
from shutil import copyfile, copytree, make_archive
import tempfile
from .object_source_alias import Alias
from .object_source_mesh import MeshSource
from .object_source_library import ObjectSourceLibrary
from .object_source_file_manager import FileManager
import bpy


class ObjectSource:

    @classmethod
    def library_to_add_on(cls, context):
        # export library to a separate add-on
        dest_path = FileManager.abs_path(context.preferences.addons[__package__].preferences.export_path)
        if dest_path and os.path.exists(dest_path):
            with tempfile.TemporaryDirectory() as temp_dir:
                folder_to_zip = FileManager.abs_path(os.path.join(temp_dir, ObjectSourceLibrary.idname))
                folder_to_zip_content = FileManager.abs_path(os.path.join(temp_dir, ObjectSourceLibrary.idname, ObjectSourceLibrary.idname))
                os.makedirs(folder_to_zip)
                # copy library source to zip folder
                copytree(ObjectSourceLibrary.library_path(), os.path.join(folder_to_zip_content, ObjectSourceLibrary.idname))
                # copy .py files
                py_files = [
                    'object_source_library.py', 'object_source_library_items.py', 'object_source_library_ops.py',
                    'object_source_library_panel.py'
                ]
                for py_file in py_files:
                    copyfile(os.path.join(os.path.dirname(FileManager.abs_path(__file__)), py_file), os.path.join(folder_to_zip_content, py_file))
                # init file with renaming
                copyfile(os.path.join(os.path.dirname(FileManager.abs_path(__file__)), 'object_source_library_template_init.py'), os.path.join(folder_to_zip_content, '__init__.py'))
                # make add-on archive
                arch = make_archive(os.path.join(dest_path, ObjectSourceLibrary.idname), 'zip', folder_to_zip)
                bpy.ops.object_source.messagebox('INVOKE_DEFAULT', message='Add-on created in:\n' + arch)
        else:
            bpy.ops.object_source.messagebox('INVOKE_DEFAULT', message='Please, specify the existed path for export.')

    @classmethod
    def object_to_library(cls, objects, context, scene_data):
        # add object to source library
        source, source_alias = cls._source(
            objects=objects,
            context=context,
            scene_data=scene_data
        )
        # save source to file
        library_path = ObjectSourceLibrary.library_path()
        source_file_name = source_alias + '.py'
        source_file_path = os.path.join(library_path, source_file_name)
        if os.path.exists(source_file_path):
            bpy.ops.object_source.messagebox('INVOKE_DEFAULT', message='Mesh with the same name already exists in the library!')
        else:
            # write to file
            with open(file=source_file_path, mode='w', encoding='utf8') as source_file:
                source_file.write(source)
            # add to library list
            library_item = context.window_manager.object_source_lib_items.add()
            library_item.name = source_alias

    @classmethod
    def object_to_text(cls, objects, context, scene_data):
        # show objects as source in TEXT_EDITOR window
        source, source_alias = cls._source(
            objects=objects,
            context=context,
            scene_data=scene_data
        )
        text_block = scene_data.texts.get(source_alias)
        if not text_block:
            text_block = scene_data.texts.new(name=source_alias)
        text_block.from_string(string=source)
        text_block.select_set(line_start=0, char_start=0, line_end=0, char_end=0)
        text_block.current_line_index = 0
        # show text object in window
        show_in_area = None
        for area in context.screen.areas:
            if area.type == 'TEXT_EDITOR':
                show_in_area = area
                break
        if not show_in_area:
            for area in context.screen.areas:
                if area.type not in ['PROPERTIES', 'OUTLINER']:
                    show_in_area = area
                    break
        if show_in_area:
            show_in_area.type = 'TEXT_EDITOR'
            show_in_area.spaces.active.text = text_block

    @classmethod
    def _source(cls, objects, context, scene_data):
        # get source for objects
        source_alias = Alias.alias(item=objects)
        # header
        source = cls._header()
        # collection
        collection_alias = 'source_collection'
        source += cls._collection(name=source_alias, alias=collection_alias)
        # objects
        current_mode = context.object.mode if context.object else 'OBJECT'
        if current_mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
        for obj in objects:
            # object data
            if obj.type == 'MESH':
                source += MeshSource.to_source(
                    obj=obj,
                    collection=collection_alias,
                    context=context,
                    scene_data=scene_data
                )
        if context.object:
            bpy.ops.object.mode_set(mode=current_mode)
        return source, source_alias

    @staticmethod
    def _header():
        # header for mesh source
        header = 'import bpy' + '\n'
        header += '\n'
        return header

    @staticmethod
    def _collection(name, alias):
        # collection for mesh source
        collection = '# COLLECTION' + '\n'
        collection += alias + ' = bpy.data.collections.new(\'' + name + '\')' + '\n'
        collection += 'bpy.context.scene.collection.children.link(source_collection)' + '\n'
        collection += '\n'
        return collection
