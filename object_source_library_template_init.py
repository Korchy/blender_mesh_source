# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_mesh_source

from . import object_source_library_items
from . import object_source_library_ops
from . import object_source_library_panel


bl_info = {
    'name': 'Object Source Library',
    'category': 'All',
    'author': 'Object Source',
    'version': (1, 0, 0),
    'blender': (2, 83, 0),
    'location': 'N-Panel > Object Source Library',
    'wiki_url': '',
    'tracker_url': '',
    'description': 'Object Source Library Distribution'
}


def register():
    object_source_library_items.register()
    object_source_library_ops.register()
    object_source_library_panel.register()


def unregister():
    object_source_library_panel.unregister()
    object_source_library_ops.unregister()
    object_source_library_items.unregister()


if __name__ == '__main__':
    register()
