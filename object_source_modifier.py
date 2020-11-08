# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_mesh_source

from .object_source_alias import Alias
from .object_source_bl_types_conversion import BlTypesConversion


class ModifierSource:

    @classmethod
    def to_source(cls, modifier, parent_expr='', deep=0):
        # get modifier source
        source = ''
        modifier_alias = Alias.alias(item=modifier).lower()
        source += ('    ' * deep) + modifier_alias + ' = ' + parent_expr + '.modifiers.new(name=\'' + \
                  modifier.name + '\', type=\'' + modifier.type + '\')' + '\n'
        # attributes
        # don't process
        excluded_attributes = [
            'bl_rna', 'name', 'rna_type', 'type'
        ]
        # process first - because they influence on other attributes
        first_attributes = [attr for attr in [] if hasattr(modifier, attr)]
        # this attributes - complex
        complex_attributes = [attr for attr in ['custom_profile'] if hasattr(modifier, attr)]
        # get source
        source += BlTypesConversion.source_from_complex_type(
            value=modifier,
            excluded_attributes=excluded_attributes,
            preordered_attributes=first_attributes,
            complex_attributes=complex_attributes,
            parent_expr=('    ' * deep) + modifier_alias,
            deep=deep
        )
        return source
