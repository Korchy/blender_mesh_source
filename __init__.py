# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_mesh_source

from . import mesh_source_ops
from . import mesh_source_ui
from . import mesh_source_preferences
from .addon import Addon
from . import object_source_message_box
from . import object_source_library_items
from . import object_source_library_ops
from . import object_source_library_panel


bl_info = {
    'name': 'Mesh_Source',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 0, 1),
    'blender': (2, 90, 0),
    'location': 'N-Panel > Mesh Source',
    'wiki_url': 'https://b3d.interplanety.org/en/blender-add-on-mesh-source/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-mesh-source/',
    'description': 'Converting meshes to Python source code'
}


def register():
    if not Addon.dev_mode():
        object_source_message_box.register()
        mesh_source_preferences.register()
        mesh_source_ops.register()
        mesh_source_ui.register()
        object_source_library_items.register()
        object_source_library_ops.register()
        object_source_library_panel.register()
    else:
        print('It seems you are trying to use the dev version of the ' + bl_info['name'] + ' add-on. It may work not properly. Please download and use the release version')


def unregister():
    if not Addon.dev_mode():
        object_source_library_panel.unregister()
        object_source_library_ops.unregister()
        object_source_library_items.unregister()
        mesh_source_ui.unregister()
        mesh_source_ops.unregister()
        mesh_source_preferences.unregister()
        object_source_message_box.unregister()


if __name__ == '__main__':
    register()
