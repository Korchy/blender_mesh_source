# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_mesh_source

import os
import bpy


class FileManager:

    @staticmethod
    def abs_path(path):
        # returns absolute file path from path
        if path[:2] == '//':
            return os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(bpy.data.filepath)), path[2:]))
        else:
            return os.path.abspath(path)
