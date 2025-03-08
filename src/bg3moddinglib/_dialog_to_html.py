from __future__ import annotations

import os
import os.path
import sys
import xml.etree.ElementTree as et

from ._common import (
    get_required_bg3_attribute,
)
from ._constants import *
from ._dialog import dialog_object


def create_ui_javascript(output_dir_path: str) -> None:
    os.makedirs(output_dir_path, exist_ok = True)
    ui_js_path = os.path.join(output_dir_path, "ui.js")
    with open(ui_js_path, "wt") as f:
        f.write("""
function get_expand_elt(div_elt) {
    for (let i = 0; i < div_elt.children.length; ++i) {
        const elt = div_elt.children[i];
        if (elt.classList.contains('expand')) {
            return elt;
        }
    }
    return null;
}
function get_collapse_elt(div_elt) {
    for (let i = 0; i < div_elt.children.length; ++i) {
        const elt = div_elt.children[i];
        if (elt.classList.contains('collapse')) {
            return elt;
        }
    }
    return null;
}
function get_children_nodes(div_elt) {
    const result = [];
    for (let i = 0; i < div_elt.children.length; ++i) {
        const elt = div_elt.children[i];
        if (elt.classList.contains('node')) {
            result.push(elt);
        }
    }
    return result;
}
function on_click_expand(uuid) {
    console.log("on_click_expand", uuid)
    const div_elt = document.getElementById(uuid);
    if (div_elt == null) {
        console.log("Can't find parent of the click target");
        return;
    }
    const exp_elt = get_expand_elt(div_elt);
    get_expand_elt(div_elt).classList.replace('visible', 'invisible')
    get_collapse_elt(div_elt).classList.replace('invisible', 'visible')
    get_children_nodes(div_elt).forEach(node => {
        node.classList.replace('invisible', 'visible-div')
    });
}
function on_click_collapse(uuid) {
    console.log("on_click_expand", uuid)
    const div_elt = document.getElementById(uuid);
    if (div_elt == null) {
        console.log("Can't find parent of the click target");
        return;
    }
    const exp_elt = get_expand_elt(div_elt);
    get_expand_elt(div_elt).classList.replace('invisible', 'visible')
    get_collapse_elt(div_elt).classList.replace('visible', 'invisible')
    get_children_nodes(div_elt).forEach(node => {
        node.classList.replace('visible-div', 'invisible')
    });
}""")

def start_dialog_html_file(d: dialog_object, output_dir_path: str) -> None:
    with open(os.path.join(output_dir_path, d.name + ".html"), "wt") as f:
        f.write("""
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>""" + d.name + """<title>
        <style>
            body {
                background-color: lightgrey;
                font-family: monospace;
                font-size: medium;
            }
            .title {
                font-family: 'Times New Roman', Times, serif;
                font-size: xx-large;
                display: block;
                padding: 10px;
            }
            .greeting {
                background-color: white;
            }
            .question {
                background-color: lightgreen;
            }
            .answer {
                background-color: lightblue;
            }
            .cinematic {
                background-color: lightpink;
            }
            .checkflags {
                margin: 5px;
            }
            .setflags {
                margin: 5px;
            }
            .tags {
                margin: 5px;
            }
            .visible {
                display: inline;
            }
            .visible-div {
                display: block;
            }
            .invisible {
                display: none;
            }
            .speaker {
                font-style: italic;
                font-weight: bolder;
            }
            .voiceline {
                font-style: normal;
                font-weight: normal;
            }
            .node {
                width: 100%;
                height: 100%;
                padding: 10px;
            }
        </style>
        <script type="text/javascript" src="scripts/ui.js"></script>
    </head>
    <body>
        <div class="title">""" + d.name + """</div>
""")

def finish_dialog_html_file(d: dialog_object, output_dir_path: str) -> None:
    with open(os.path.join(output_dir_path, d.name + ".html"), "at") as f:
        f.write("""
    </body>
</html>""")

def get_speaker(d: dialog_object, idx: int) -> str:
    speaker_uuid = d.get_speaker_by_index(idx)
    return SPEAKER_NAME[speaker_uuid]

        

def convert_dialog_to_html(d: dialog_object, output_dir_path: str) -> None:
    sys.setrecursionlimit(10000)
    dialog_nodes = { get_required_bg3_attribute(node, 'UUID') : node for node in d.get_dialog_nodes() }
    
    greetings_uuids = d.get_root_nodes()

    def generate_dialog_node_html(dialog_node_uuid: str, html: list[str]) -> None:
        dialog_node = dialog_nodes[dialog_node_uuid]



