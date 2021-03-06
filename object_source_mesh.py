# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_mesh_source

from .object_source_alias import Alias
from .object_source_bl_types_conversion import BlTypesConversion
from .object_source_modifier import ModifierSource


class MeshSource:

    @classmethod
    def to_source(cls, obj, collection, context, scene_data):
        # convert mesh to source
        source = '# MESH' + '\n'
        object_alias = Alias.alias(item=obj)
        mesh_alias = Alias.alias(item=obj.data)
        # mesh
        source += 'vertices = ' + str([(vert.co.x, vert.co.y, vert.co.z) for vert in obj.data.vertices]) + '\n'
        source += 'edges = ' + str([[vert for vert in edge.vertices] for edge in obj.data.edges]) + '\n'
        source += 'faces = ' + str([[vert for vert in polygon.vertices] for polygon in obj.data.polygons]) + '\n'
        source += 'new_mesh = bpy.data.meshes.new(\'' + mesh_alias + '\')' + '\n'
        source += 'new_mesh.from_pydata(vertices, edges, faces)' + '\n'
        source += 'new_mesh.update()' + '\n'
        # create object
        source += 'new_object = bpy.data.objects.new(name=\'' + object_alias + '\', object_data=new_mesh)' + '\n'
        # add object to collection
        source += collection + '.objects.link(new_object)' + '\n'
        # location
        source += '# position' + '\n'
        source += 'new_object.location = ' + BlTypesConversion.source_by_type(
            item=obj,
            value=obj.location
        ) + '\n'
        source += 'new_object.rotation_euler = ' + BlTypesConversion.source_by_type(
            item=obj,
            value=obj.rotation_euler
        ) + '\n'
        source += 'new_object.scale = ' + BlTypesConversion.source_by_type(
            item=obj,
            value=obj.scale
        ) + '\n'
        # shade flat/smooth
        source += '# flat/smooth' + '\n'
        source += 'smooth_data = ' + str([polygon.use_smooth for polygon in obj.data.polygons]) + '\n'
        source += 'for i, polygon in enumerate(new_object.data.polygons):' + '\n'
        source += '    ' + 'polygon.use_smooth = (True if smooth_data[i] else False)'+ '\n'
        # vertex groups
        if obj.vertex_groups:
            source += '# vertex groups' + '\n'
            for vertex_group in obj.vertex_groups:
                source += 'vertex_group_data = ' + str([vert.index for vert in obj.data.vertices if obj.vertex_groups[vertex_group.name].index in [i.group for i in vert.groups]]) + '\n'
                source += 'vertex_group = new_object.vertex_groups.new(name=\'' + vertex_group.name + '\')' + '\n'
                source += 'vertex_group.add(vertex_group_data, 1.0, \'ADD\')' + '\n'
        # UVs
        if obj.data.uv_layers:
            source += '# UVs' + '\n'
            for uv in obj.data.uv_layers:
                source += 'uv_xy = ' + str([(data.uv.x, data.uv.y) for data in uv.data]) + '\n'
                source += 'new_uv = new_object.data.uv_layers.new(name=\'' + uv.name + '\')' + '\n'
                source += 'for loop in new_object.data.loops:' + '\n'
                source += '    ' + 'new_uv.data[loop.index].uv = uv_xy[loop.index]' + '\n'
        # Modifiers
        if obj.modifiers:
            source += '# modifiers' + '\n'
            for modifier in obj.modifiers:
                source += ModifierSource.to_source(
                    modifier=modifier,
                    parent_expr='new_object'
                )
        # update
        source += '# UPDATE' + '\n'
        source += 'new_object.data.update()' + '\n'
        return source + '\n'
