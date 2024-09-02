import bg3moddinglib as bg3
import xml.etree.ElementTree as et

from .fixtures import *

def test_bg3_game_object_dialog(bg3_modding_env, tmp_path):
    tool = bg3.bg3_modding_tool(bg3_modding_env)
    
    lsf = tool.unpack("test", "lsf_dialog/test_dialog.lsf")
    assert lsf

    lsf_lsx = tool.convert_lsf_to_lsx(lsf)
    assert lsf_lsx

    dialog_obj = bg3.bg3_game_object_dialog(lsf_lsx)
    speakers = dialog_obj.speakers
    assert speakers[0] == ('c7c13742-bacd-460a-8f65-f864fe41f255', '1e0f2076-e47e-28c5-d016-d2ab809dd53a')
    assert speakers[1] == ('e0d1ff71-04a8-4340-ae64-9684d846eb83', 'a4b1af84-6f5f-9859-1a34-53ec4bf179a8')

    root_nodes = dialog_obj.root_nodes
    assert root_nodes[0] == '8fea79c6-5257-36a9-b979-979ba23c1eaf'
    assert root_nodes[1] == '7d4e7cfc-a5e1-51e1-ca39-fef1523df51c'
    assert root_nodes[2] == '67d74304-76ec-a29c-dad8-8a4a9cfa51fe'

    e = dialog_obj.get_dialog_node('c455ee8a-12a6-b66f-33f3-7f738b76e65b')
    assert e
    attributes = bg3.get_node_attributes(e)
    attributes['constructor'] == 'TagAnswer'
    attributes['UUID'] == 'c455ee8a-12a6-b66f-33f3-7f738b76e65b'
    attributes['speaker'] == '0'
    tier1 = bg3.get_node_children_as_dict(e)
    assert len(tier1) == 6
    assert tier1['TaggedTexts']
    tier2 = bg3.get_node_children(tier1['TaggedTexts'])
    assert tier2
    assert len(tier2) == 1
    tier3 = bg3.get_node_children_as_dict(tier2[0])
    assert tier3
    assert len(tier3) == 2
    tier4 = bg3.get_node_children(tier3['TagTexts'])
    assert tier4
    assert len(tier4) == 1
    assert tier4[0].get('id') == 'TagText'
    attributes = bg3.get_node_attributes(tier4[0])
    assert attributes['TagText'] == 'h352f85c1gf8ffg4e64g9ec6g57a4f2c02a42'
    assert attributes['LineId'] == '1f8c225d-c869-4a96-bdb3-01d57668637c'

    e = dialog_obj.get_dialog_node('96d4aaf8-ca02-1482-f7bb-a5e4c6e81ae3')
    assert e
    attributes = bg3.get_node_attributes(e)
    attributes['constructor'] == 'TagAnswer'
    attributes['UUID'] == '96d4aaf8-ca02-1482-f7bb-a5e4c6e81ae3'
    attributes['speaker'] == '0'
    tier1 = bg3.get_node_children_as_dict(e)
    assert tier1
    assert len(tier1) == 6
    tier2 = bg3.get_node_children(tier1['setflags'])
    assert tier2
    assert len(tier2) == 2

    dialog_obj.patch_dialog_node('96d4aaf8-ca02-1482-f7bb-a5e4c6e81ae3', [et.fromstring("""<node id="setflags" />""")])
    dialog_obj.delete_dialog_node('c455ee8a-12a6-b66f-33f3-7f738b76e65b')
    new_node = """
    <node id="node" key="UUID">
        <attribute id="constructor" type="FixedString" value="Alias" />
        <attribute id="UUID" type="FixedString" value="ea978f9b-5257-36a9-b979-79c6a23c1eaf" />
        <children>
            <node id="GameData" />
            <node id="Tags" />
            <node id="setflags" />
            <node id="checkflags" />
        </children>
    </node>"""
    dialog_obj.add_dialog_node(et.fromstring(new_node))

    saved_file_path = os.path.join(tmp_path, 'test_dialog.lsf.lsx')
    dialog_obj.save_to(saved_file_path)

    lsf = tool.convert_lsx_to_lsf(saved_file_path)
    lsf_lsx = tool.convert_lsf_to_lsx(lsf)
    dialog_obj = bg3.bg3_game_object_dialog(lsf_lsx)
    assert dialog_obj

    speakers = dialog_obj.speakers
    assert speakers[0] == ('c7c13742-bacd-460a-8f65-f864fe41f255', '1e0f2076-e47e-28c5-d016-d2ab809dd53a')
    assert speakers[1] == ('e0d1ff71-04a8-4340-ae64-9684d846eb83', 'a4b1af84-6f5f-9859-1a34-53ec4bf179a8')

    root_nodes = dialog_obj.root_nodes
    assert root_nodes[0] == '8fea79c6-5257-36a9-b979-979ba23c1eaf'
    assert root_nodes[1] == '7d4e7cfc-a5e1-51e1-ca39-fef1523df51c'
    assert root_nodes[2] == '67d74304-76ec-a29c-dad8-8a4a9cfa51fe'

    with pytest.raises(KeyError):
        dialog_obj.get_dialog_node('c455ee8a-12a6-b66f-33f3-7f738b76e65b')

    e = dialog_obj.get_dialog_node('96d4aaf8-ca02-1482-f7bb-a5e4c6e81ae3')
    assert e
    attributes = bg3.get_node_attributes(e)
    attributes['constructor'] == 'TagAnswer'
    attributes['UUID'] == '96d4aaf8-ca02-1482-f7bb-a5e4c6e81ae3'
    attributes['speaker'] == '0'
    tier1 = bg3.get_node_children_as_dict(e)
    assert tier1
    assert len(tier1) == 6
    tier2 = bg3.get_node_children(tier1['setflags'])
    assert not tier2
    assert len(tier2) == 0

    e = dialog_obj.get_dialog_node('ea978f9b-5257-36a9-b979-79c6a23c1eaf')
    assert e
