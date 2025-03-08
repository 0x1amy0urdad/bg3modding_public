from __future__ import annotations

import os
import uuid
import xml.etree.ElementTree as et
import numpy as np

from typing import Callable

def new_random_uuid() -> str:
    return str(uuid.uuid4())

def translate_path(in_path: str) -> str:
    parts = in_path.replace('\\', '/').split('/')
    if ':' in parts[0]:
        parts[0] += "\\"
    return os.path.join(*parts)

def to_compact_string(xml_node: et.Element) -> str:
    return et.tostring(xml_node).decode('utf-8').replace('\t', '').replace('\n', '').replace('\r', '')

def get_bg3_attribute(node: et.Element, attribute_name: str, /, value_name: str | None = None) -> str | None:
    attribute_node = node.find(f'./attribute[@id="{attribute_name}"]')
    if attribute_node is None:
        return None
    effective_value_name = "value" if value_name is None else value_name
    return attribute_node.get(effective_value_name)

def get_required_bg3_attribute(node: et.Element, attribute_name: str, /, value_name: str | None = None) -> str:
    attribute_node = node.find(f'./attribute[@id="{attribute_name}"]')
    if attribute_node is None:
        raise ValueError(f"required BG3 attribute {attribute_name} doesn't exist")
    effective_value_name = "value" if value_name is None else value_name
    value = attribute_node.get(effective_value_name)
    if value is None:
        raise ValueError(f"required BG3 attribute {attribute_name} doesn't have a value")
    return value

def get_bg3_handle_attribute(node: et.Element, attribute_name: str, /, value_name: str | None = None) -> tuple[str, int]:
    attribute_node = node.find(f'./attribute[@id="{attribute_name}"]')
    if attribute_node is None:
        raise ValueError(f"required BG3 attribute {attribute_name} doesn't exist")
    effective_value_name = "handle" if value_name is None else value_name
    value = attribute_node.get(effective_value_name)
    if value is None:
        raise ValueError(f"required BG3 attribute {attribute_name} doesn't have a value")
    version = int(attribute_node.get('version'))
    return (value, version)

def set_bg3_attribute(
        node: et.Element,
        attribute_name: str,
        attribute_value: str,
        /,
        attribute_type: str = "",
        version: int | None = None
    ) -> None:
    attribute_node = node.find(f'./attribute[@id="{attribute_name}"]')
    if attribute_node is None:
        if not attribute_type:
            raise ValueError(f"attribute type is required to create a new attribute {attribute_name}")
        if version is not None:
            attribute_node = et.fromstring(f'<attribute id="{attribute_name}" type="{attribute_type}" handle="{attribute_value} version="{version}" />')
            attribute_node.set('version', str(version))
        else:
            attribute_node = et.fromstring(f'<attribute id="{attribute_name}" type="{attribute_type}" value="{attribute_value}" />')
        node.append(attribute_node)
    else:
        if attribute_type:
            attribute_node.set("type", attribute_type)
        if version is not None:
            attribute_node.set("handle", attribute_value)
            attribute_node.set("version", str(version))
        else:
            attribute_node.set("value", attribute_value)

def has_bg3_attribute(node: et.Element, attribute_name: str) -> bool:
    return node.find(f'./attribute[@id="{attribute_name}"]') is not None

def get_required_attribute(node: et.Element, attribute_name: str) -> str:
    result = node.get(attribute_name)
    if result is None:
        raise ValueError(f"required attribute {attribute_name} doesn't exist")
    return result

def lower_bound_by_node_attribute(nodes: list[et.Element], attribute_name: str, target_value: str) -> int:
    return lower_bound(nodes, lambda node: get_required_attribute(node, attribute_name), target_value)

def lower_bound_by_bg3_attribute(nodes: list[et.Element], attribute_name: str, target_value: str) -> int:
    return lower_bound(nodes, lambda node: get_required_bg3_attribute(node, attribute_name), target_value)

def lower_bound(nodes: list[et.Element], attribute_getter: Callable[[et.Element], str], target_value: str) -> int:
    top = len(nodes)
    if top == 1:
        return 0
    pos = top >> 1
    step = pos >> 1
    for n in range(0, top):
        cur = attribute_getter(nodes[pos])
        next = None if pos + 1 >= top else attribute_getter(nodes[pos + 1])
        prev = None if pos == 0 else attribute_getter(nodes[pos - 1])
        if cur < target_value:
            if next is None or next > target_value:
                return pos
            if step > 1:
                step = step >> 1
            pos += step
        elif cur == target_value:
            return pos
        else:
            if prev is None or prev < target_value:
                return pos
            if step > 1:
                step = step >> 1
            pos -= step
    raise RuntimeError(f"Failed to find the lower bound for {target_value}")

def find_object_by_map_key(target: et.Element, key: str) -> et.Element | None:
    objs = target.findall('./children/node[@id="Object"]')
    for obj in objs:
        obj_key = get_bg3_attribute(obj, 'MapKey')
        if key == obj_key:
            return obj
    return None

def put_object_into_map(target: et.Element, obj: et.Element) -> None:
    obj_key = get_bg3_attribute(obj, 'MapKey')
    existing_obj = find_object_by_map_key(target, obj_key)
    if existing_obj is not None:
        children = target.find('./children')
        if isinstance(children, et.Element):
            children.remove(existing_obj)
            children.append(obj)
        else:
            children = et.fromstring('<children></children>')
            children.append(obj)
            target.append(children)

def remove_object_by_map_key(target: et.Element, key: str) -> None:
    children = target.find('./children')
    if not isinstance(children, et.Element):
        raise KeyError(f"object '{key}' doesn't exist in the map")
    existing_obj = find_object_by_map_key(target, key)
    if existing_obj is None:
        raise KeyError(f"object '{key}' doesn't exist in the map")
    children.remove(existing_obj)

def euler_to_quaternion(x_deg: float, y_deg: float, z_deg: float, sequence: str = 'xyz') -> tuple[float, float, float, float]:
    a1 = np.deg2rad(x_deg)
    a2 = np.deg2rad(y_deg)
    a3 = np.deg2rad(z_deg)

    a1_2 = a1 / 2
    a2_2 = a2 / 2
    a3_2 = a3 / 2

    c1 = np.cos(a1_2)
    s1 = np.sin(a1_2)
    c2 = np.cos(a2_2)
    s2 = np.sin(a2_2)
    c3 = np.cos(a3_2)
    s3 = np.sin(a3_2)

    calculations = {
        'xyz': lambda: (
            c1*c2*c3 - s1*s2*s3,  # w
            s1*c2*c3 + c1*s2*s3,  # x
            c1*s2*c3 - s1*c2*s3,  # y
            c1*c2*s3 + s1*s2*c3   # z
        ),
        'xzy': lambda: (
            c1*c2*c3 + s1*s2*s3,  # w
            s1*c2*c3 - c1*s2*s3,  # x
            c1*s2*c3 - s1*c2*s3,  # y
            c1*c2*s3 + s1*s2*c3   # z
        ),
        'yxz': lambda: (
            c1*c2*c3 + s1*s2*s3,  # w
            c1*s2*c3 + s1*c2*s3,  # x
            s1*c2*c3 - c1*s2*s3,  # y
            c1*c2*s3 - s1*s2*c3   # z
        ),
        'yzx': lambda: (
            c1*c2*c3 - s1*s2*s3,  # w
            c1*s2*c3 + s1*c2*s3,  # x
            s1*c2*c3 + c1*s2*s3,  # y
            c1*c2*s3 - s1*s2*c3   # z
        ),
        'zxy': lambda: (
            c1*c2*c3 - s1*s2*s3,  # w
            c1*c2*s3 + s1*s2*c3,  # x
            c1*s2*c3 + s1*c2*s3,  # y
            s1*c2*c3 - c1*s2*s3   # z
        ),
        'zyx': lambda: (
            c1*c2*c3 + s1*s2*s3,  # w
            c1*c2*s3 - s1*s2*c3,  # x
            c1*s2*c3 + s1*c2*s3,  # y
            s1*c2*c3 - c1*s2*s3   # z
        )
    }
    if sequence not in calculations:
        raise ValueError(f"rotation sequence '{sequence}' not supported")
    w, x, y, z = calculations[sequence]()

    norm = np.sqrt(w * w + x * x + y * y + z * z)
    return (float(x / norm), float(y / norm), float(z / norm), float(w / norm))

def quaternion_to_euler(x: float, y: float, z: float, w: float, sequence: str = 'xyz') -> tuple[float, float, float]:
    sequence = sequence.lower()

    r11 = 1         - 2 * y * y - 2 * z * z
    r12 = 2 * x * y - 2 * w * z
    r13 = 2 * x * z + 2 * w * y
    r21 = 2 * x * y + 2 * w * z
    r22 = 1         - 2 * x * x - 2 * z * z
    r23 = 2 * y * z - 2 * w * x
    r31 = 2 * x * z - 2 * w * y
    r32 = 2 * y * z + 2 * w * x
    r33 = 1         - 2 * x * x - 2 * y * y

    match sequence:
        case 'xyz':
            x_rad = np.arctan2(-r23, r33)
            y_rad = np.arcsin(r13)
            z_rad = np.arctan2(-r12, r11)
        case 'xzy':
            x_rad = np.arctan2(r32, r22)
            z_rad = np.arctan2(r13, r11)
            y_rad = np.arcsin(-r12)
        case 'yxz':
            y_rad = np.arcsin(-r23)
            x_rad = np.arctan2(r13, r33)
            z_rad = np.arctan2(r21, r22)
        case 'yzx':
            y_rad = np.arctan2(-r13, r11)
            z_rad = np.arctan2(-r23, r22)
            x_rad = np.arcsin(r21)
        case 'zxy':
            z_rad = np.arctan2(-r31, r33)
            x_rad = np.arcsin(r32)
            y_rad = np.arctan2(-r12, r22)
        case 'zyx':
            z_rad = np.arcsin(-r31)
            y_rad = np.arctan2(r32, r33)
            x_rad = np.arctan2(r21, r11)
        case _:
            raise ValueError(f"Rotation sequence '{sequence}' not supported")

    return float(np.rad2deg(x_rad)), float(np.rad2deg(y_rad)), float(np.rad2deg(z_rad))
