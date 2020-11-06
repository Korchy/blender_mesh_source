# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_mesh_source

from .object_source_alias import Alias


class MeshSource:

    @classmethod
    def to_source(cls, obj, collection, context, scene_data):
        # convert mesh to source
        source = '# MESH' + '\n'
        object_alias = Alias.alias(item=obj)
        mesh_alias = Alias.alias(item=obj.data)
        # mesh
        source += 'vertices = ' + str([(vert.co.x, vert.co.y, vert.co.z) for vert in obj.data.vertices]) + '' + '\n'
        source += 'edges = ' + str([[vert for vert in edge.vertices] for edge in obj.data.edges]) + '' + '\n'
        source += 'faces = ' + str([[vert for vert in polygon.vertices] for polygon in obj.data.polygons]) + '' + '\n'
        source += 'new_mesh = bpy.data.meshes.new(\'' + mesh_alias + '\')' + '\n'
        source += 'new_mesh.from_pydata(vertices, edges, faces)' + '\n'
        source += 'new_mesh.update()' + '\n'
        # create object
        source += 'new_object = bpy.data.objects.new(name=\'' + object_alias + '\', object_data=new_mesh)' + '\n'
        # add object to collection
        source += collection + '.objects.link(new_object)' + '\n'
        return source
