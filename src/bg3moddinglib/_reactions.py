from __future__ import annotations

import xml.etree.ElementTree as et

from ._common import get_required_bg3_attribute, new_random_uuid
from ._constants import SPEAKER_TO_ORIGIN_MAP
from ._files import game_file, game_files

class reaction_object:
    __file: game_file
    __uuid: str
    __scope: int
    __reactions: dict[str, int]

    def __init__(self, f: game_file, /, reactions: dict[str, int] | None = None, uuid: str | None = None, scope: int = 1) -> None:
        root = f.xml.getroot()
        if not isinstance(root, et.Element):
            raise ValueError('unexpected XML content')
        if root.find('./region[@id="Reactions"]') is None:
            uuid = new_random_uuid() if uuid is None else uuid
            root.append(et.fromstring('<version major="4" minor="0" revision="9" build="328"/>'))
            root.append(et.fromstring('<region id="Reactions"><node id="root"><children><node id="Reaction">'
                                      + f'<attribute id="Scope" type="uint8" value="{scope}"/>'
                                      + f'<attribute id="UUID" type="guid" value="{uuid}"/><children>'
                                      + '<node id="Reactions"><children></children></node></children></node></children></node></region>'))
            children_node = root.find('./region[@id="Reactions"]/node[@id="root"]/children/node[@id="Reaction"]/children/node[@id="Reactions"]/children')
            if not isinstance(children_node, et.Element):
                raise ValueError('unexpected: not an Element')
            for k, v in reactions.items():
                if k in SPEAKER_TO_ORIGIN_MAP:
                    k = SPEAKER_TO_ORIGIN_MAP[k]
                children_node.append(et.fromstring(f'<node id="Reaction"><attribute id="id" type="guid" value="{k}"/><attribute id="value" type="int32" value="{v}"/></node>'))
            self.__file = f
            self.__uuid = uuid
            self.__scope = scope
            self.__reactions = reactions if isinstance(reactions, dict) else dict[str, int]()
        else:
            top_reaction_node = root.find('./region[@id="Reactions"]/node[@id="root"]/children/node[@id="Reaction"]')
            if not isinstance(top_reaction_node, et.Element):
                raise ValueError(f'failed to parse reactions from file {f.relative_file_path}')
            reactions_node = top_reaction_node.find('./children/node[@id="Reactions"]')
            if not isinstance(reactions_node, et.Element):
                raise ValueError(f'failed to parse reactions from file {f.relative_file_path}')
            reactions_nodes = reactions_node.findall('./children/node[@id="Reaction"]')
            reactions = dict[str, int]()
            for reaction_node in reactions_nodes:
                character_uuid = get_required_bg3_attribute(reaction_node, "id")
                approval_value = int(get_required_bg3_attribute(reaction_node, "value"))
                if isinstance(character_uuid, str) and isinstance(approval_value, int):
                    reactions[character_uuid] = approval_value
                else:
                    raise ValueError(f'failed to parse reactions from file {f.relative_file_path}')
            self.__file = f
            self.__uuid = get_required_bg3_attribute(top_reaction_node, 'UUID')
            self.__scope = int(get_required_bg3_attribute(top_reaction_node, 'Scope'))
            self.__reactions = reactions

    @staticmethod
    def open_existing(files: game_files, uuid: str) -> reaction_object:
        try:
            f = files.get_file('Gustav', f'Public/GustavDev/ApprovalRatings/Reactions/{uuid}.lsx')
        except:
            f = None
        if f is None:
            try:
                f = files.get_file('Gustav', f'Public/Gustav/ApprovalRatings/Reactions/{uuid}.lsx')
            except:
                f = None
        if f is None:
            raise FileNotFoundError(f'reaction is not found: {uuid}')
        return reaction_object(f)

    @staticmethod
    def create_new(files: game_files, reactions: dict[str, int], /, uuid: str | None = None, scope: int = 1) -> reaction_object:
        if uuid is None:
            uuid = new_random_uuid()
        f = files.add_new_file(f'Public/GustavDev/ApprovalRatings/Reactions/{uuid}.lsx')
        return reaction_object(f, reactions, uuid = uuid, scope = scope)

    @property
    def file(self) -> game_file:
        return self.__file

    @property
    def scope(self) -> int:
        return self.__scope

    @property
    def uuid(self) -> str:
        return self.__uuid

    @property
    def reactions(self) -> dict[str, int]:
        return self.__reactions.copy()
