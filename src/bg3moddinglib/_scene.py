from __future__ import annotations

import xml.etree.ElementTree as et

from ._common import get_bg3_attribute, get_required_bg3_attribute, new_random_uuid, to_compact_string, put_object_into_map, find_object_by_map_key
from ._files import game_file

from typing import Iterable

class scene_object:
    DEFAULT_STAGE_UUID: str = '00000000-0000-0000-0000-000000000000'

    __lsf_file: game_file
    __lsx_file: game_file
    __current_stage_uuid: str | None

    def __init__(self, lsf_file: game_file, lsx_file: game_file) -> None:
        self.__lsf_file = lsf_file
        self.__lsx_file = lsx_file
        self.__current_stage_uuid = None

    @property
    def current_stage_uuid(self) -> str:
        if self.__current_stage_uuid is None:
            raise ValueError('no stage has been created yet')
        return self.__current_stage_uuid

    @property
    def lsf_xml(self) -> et.Element:
        return self.__lsf_file.root_node

    @property
    def lsx_xml(self) -> et.Element:
        return self.__lsx_file.root_node

    def create_new_stage(self, /, stage_uuid: str | None = None, name: str | None = None) -> str:
        if stage_uuid is None:
            stage_uuid = new_random_uuid()
        if name is None:
            name = "Unnamed stage"
        self.__current_stage_uuid = stage_uuid

        new_stage = et.fromstring(''.join([
            '<node id="TLStage">',
            f'<attribute id="Identifier" type="guid" value="{self.__current_stage_uuid}" />',
            f'<attribute id="Name" type="LSString" value="{name}" />',
            '</node>'
        ]))

        root_node = self.__lsf_file.xml.getroot()
        scene_children = root_node.find('./region[@id="TLScene"]/node[@id="TLScene"]/children')
        if not isinstance(scene_children, et.Element):
            raise ValueError(f"{self.__lsf_file.relative_file_path} is not a valid scene")
        stages = scene_children.find('./node[@id="TLStages"]')
        if not isinstance(stages, et.Element):
            stages = et.fromstring('<node id="TLStages"><children></children></node>')
            scene_children.append(stages)
        stages_children = stages.find('./children')
        if not isinstance(stages_children, et.Element):
            stages_children = et.fromstring('<children></children>')
            stages.append(stages_children)
        stages_children.append(new_stage)

        root_node = self.__lsx_file.xml.getroot()
        scene_children = root_node.find('./region[@id="TLScene"]/node[@id="root"]/children')
        if not isinstance(scene_children, et.Element):
            raise ValueError(f"{self.__lsx_file.relative_file_path} is not a valid scene")
        stages = scene_children.find('./node[@id="TLStages"]')
        if not isinstance(stages, et.Element):
            stages = et.fromstring('<node id="TLStages"><children></children></node>')
            scene_children.append(stages)
        stages_children = stages.find('./children')
        if not isinstance(stages_children, et.Element):
            stages_children = et.fromstring('<children></children>')
            stages.append(stages_children)
        stages_children.append(new_stage)

        return stage_uuid

    def set_actor_transform_to_stage(
            self,
            template_uuid: str,
            position: tuple[float, float, float],
            rotation: tuple[float, float, float, float],
            scale: float,
            /,
            stage_uuid: str | None
    ) -> None:
        root_node = self.__lsf_file.xml.getroot()
        actors = root_node.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]')
        found = False
        for actor in actors:
            tpl_uuid = get_bg3_attribute(actor, 'TemplateId')
            if isinstance(tpl_uuid, str) and tpl_uuid == template_uuid:
                self.__put_transform_into_stage_lsf(actor, position, rotation, scale, stage_uuid = stage_uuid)
                found = True
                break
        if not found:
            raise ValueError(f'cannot find actor {template_uuid} in {self.__lsf_file.relative_file_path}')

        found = False
        root_node = self.__lsx_file.xml.getroot()
        actors = root_node.findall('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]')
        for actor in actors:
            tpl_uuid = get_bg3_attribute(actor, 'TemplateId')
            if isinstance(tpl_uuid, str) and tpl_uuid == template_uuid:
                self.__put_transform_into_stage_lsx(actor, position, rotation, scale, stage_uuid = stage_uuid)
                found = True
                break
        if not found:
            raise ValueError(f'cannot find actor {template_uuid} in {self.__lsx_file.relative_file_path}')

    def set_camera_transform_in_stage(
            self,
            camera_uuid: str,
            position: tuple[float, float, float],
            rotation: tuple[float, float, float, float],
            scale: float,
            /,
            stage_uuid: str | None
    ) -> None:
        found = False
        root_node = self.__lsf_file.xml.getroot()
        cameras = root_node.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLCameras"]/children/node[@id="Object"]/children/node[@id="TLCameras"]')
        for camera in cameras:
            identifier = get_required_bg3_attribute(camera, 'Identifier')
            if identifier == camera_uuid:
                self.__put_transform_into_stage_lsf(camera, position, rotation, scale, stage_uuid = stage_uuid)
                found = True
                break
        if not found:
            raise ValueError(f'cannot find camera {camera_uuid} in {self.__lsf_file.relative_file_path}')

        found = False
        root_node = self.__lsx_file.xml.getroot()
        cameras = root_node.findall('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="TLCameras"]/children/node[@id="Object"]/children/node[@id="TLCameras"]')
        for camera in cameras:
            identifier = get_required_bg3_attribute(camera, 'Identifier')
            if identifier == camera_uuid:
                self.__put_transform_into_stage_lsx(camera, position, rotation, scale, stage_uuid = stage_uuid)
                found = True
                break
        if not found:
            raise ValueError(f'cannot find camera {camera_uuid} in {self.__lsf_file.relative_file_path}')

    def add_lights_to_camera(self, camera_uuid: str, lights_uuids: Iterable[str], /, stage_uuid: str | None = None) -> None:
        if stage_uuid is None:
            stage_uuid = self.__current_stage_uuid
        if stage_uuid is None:
            raise ValueError("can't add lights, either create a new stage or pass stage uuid to this call")

        lights_uuids = set(lights_uuids)

        new_lights = list[et.Element]()
        for light_uuid in lights_uuids:
            new_lights.append(et.fromstring(f'<node id="MapValue"><attribute id="Object" type="guid" value="{light_uuid}"/></node>'))
        root_node = self.__lsf_file.xml.getroot()
        cameras = root_node.find('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLCameras"]')
        if not isinstance(cameras, et.Element):
            raise RuntimeError(f'bad stage file {self.__lsf_file.relative_file_path}')
        camera = find_object_by_map_key(cameras, camera_uuid)
        if camera is None:
            raise KeyError(f'camera {camera_uuid} is not found in {self.__lsf_file.relative_file_path}')
        lights = camera.find('./children/node[@id="TLCameras"]/children/node[@id="LinkedLights"]')
        self.__add_lights(lights, new_lights, lights_uuids, stage_uuid)

        new_lights = list[et.Element]()
        for light_uuid in lights_uuids:
            new_lights.append(et.fromstring(f'<node id="MapValue"><attribute id="Object" type="guid" value="{light_uuid}"/></node>'))
        root_node = self.__lsx_file.xml.getroot()
        cameras = root_node.find('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="TLCameras"]')
        if not isinstance(cameras, et.Element):
            raise RuntimeError(f'bad stage file {self.__lsx_file.relative_file_path}')
        camera = find_object_by_map_key(cameras, camera_uuid)
        if camera is None:
            raise KeyError(f'camera {camera_uuid} is not found in {self.__lsx_file.relative_file_path}')
        lights = camera.find('./children/node[@id="TLCameras"]/children/node[@id="LinkedLights"]')
        self.__add_lights(lights, new_lights, lights_uuids, stage_uuid)

    def __add_lights(self, lights: Iterable[et.Element], new_lights: Iterable[et.Element], lights_uuids: set[str], stage_uuid: str) -> None:
        stage_lights = find_object_by_map_key(lights, stage_uuid)
        children = stage_lights.find('./children')
        if children is None:
            children = et.fromstring('<children></children>')
            for light in new_lights:
                children.append(light)
            stage_lights.append(children)
        else:
            existing_lights = children.findall('./node[@id="Object"]')
            for existing_light in existing_lights:
                light_uuid = get_required_bg3_attribute(existing_light, 'Object')
                if light_uuid in lights_uuids:
                    raise ValueError(f"duplicate light: {light_uuid}")
            for light in new_lights:
                children.append(light)

    def __put_transform_into_stage_lsf(
            self,
            target: et.Element,
            position: tuple[float, float, float],
            rotation: tuple[float, float, float, float],
            scale: float,
            /,
            stage_uuid: str | None
    ) -> None:
        if stage_uuid is None:
            stage_uuid = self.__current_stage_uuid
        new_transform = et.fromstring(''.join([
                '<node id="Object">',
                f'<attribute id="MapKey" type="guid" value="{stage_uuid}" />',
                '<children><node id="MapValue">',
                f'<attribute id="Position" type="fvec3" value="{position[0]} {position[1]} {position[2]}" />',
                f'<attribute id="RotationQuat" type="fvec4" value="{rotation[0]} {rotation[1]} {rotation[2]} {rotation[3]}" />',
                f'<attribute id="Scale" type="float" value="{scale}" />',
                '</node></children></node>'
        ]))
        transforms_map = target.find('./children/node[@id="Transform"]')
        if not isinstance(transforms_map, et.Element):
            raise ValueError(f'cannot add a new transform to stage {stage_uuid} {to_compact_string(target)}')
        put_object_into_map(transforms_map, new_transform)

    def __put_transform_into_stage_lsx(
            self,
            target: et.Element,
            position: tuple[float, float, float],
            rotation: tuple[float, float, float, float],
            scale: float,
            /,
            stage_uuid: str | None
    ) -> None:
        if stage_uuid is None:
            stage_uuid = self.__current_stage_uuid
        new_transform = et.fromstring(''.join([
                '<node id="Object">',
                f'<attribute id="MapKey" type="guid" value="{stage_uuid}" />',
                '<children><node id="MapValue">',
                f'<attribute id="Position" type="fvec3"><float3 x="{position[0]}" y="{position[1]}" z="{position[2]}"/></attribute>',
                f'<attribute id="RotationQuat" type="fvec4"><float4 x="{rotation[0]}" y="{rotation[1]}" z="{rotation[2]}" w="{rotation[3]}"/></attribute>',
                f'<attribute id="Scale" type="float" value="{scale}" />',
                '</node></children></node>'
        ]))
        transforms_map = target.find('./children/node[@id="Transform"]')
        if not isinstance(transforms_map, et.Element):
            raise ValueError(f'cannot add a new transform to stage {stage_uuid} {to_compact_string(target)}')
        put_object_into_map(transforms_map, new_transform)
