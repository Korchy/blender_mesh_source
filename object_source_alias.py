# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_mesh_source


class Alias:

    @staticmethod
    def alias(item):
        # get text alias-name for objects
        alias = ''
        if isinstance(item, (list, tuple)):
            if item:
                alias = item[0].name
                if len(item) > 1:
                    alias += '_and_' + str(len(item) - 1) + '_oth'
        else:
            alias = item.name
        if alias:
            for ch in (' ', '.', '/', '-'):
                alias = alias.replace(ch, '_')
        return alias
