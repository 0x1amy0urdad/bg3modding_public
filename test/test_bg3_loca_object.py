import bg3moddinglib as bg3

from .fixtures import *

from random import randint

def test_bg3_loca_object(bg3_modding_env, tmp_path):
    tool = bg3.bg3_modding_tool(bg3_modding_env)
    
    loca = tool.unpack("test", "loca/test_loca.loca")
    assert loca
    
    loca_xml = tool.convert_loca_to_xml(loca)
    assert loca_xml
    
    loca_obj = bg3.bg3_loca_object(loca_xml)
    assert loca_obj
    assert loca_obj.get('h000006d4gcefbg4092gbb39gfeb27a3bb0a7') == """Sorry, darling, I haven't got time for underlings."""
    assert loca_obj.get('haaaa11feg0be5g4f09g978eg030b3e2e62c6') == """Replace Spell"""
    assert loca_obj.get('hfff11ac6ge2f4g4104gbc6fg246521189b73') == """If that's her 'formula' I can smell, it's even fouler than her blood. Gods below..."""

    extra_content_uids = []
    deleted_content_uids = []
    for i in range(0, 1000):
        if i % 10 == 0 and i > 20:
            j = i - randint(1, 9)
            deleted_content_uids.append(extra_content_uids[j])
            loca_obj.delete(extra_content_uids[j])
        extra_content_uids.append(loca_obj.add("Extra content " + str(i), "1"))

    loca_obj.patch('haaaa11feg0be5g4f09g978eg030b3e2e62c6', 'Patched Content')
    loca_obj.delete('h000006d4gcefbg4092gbb39gfeb27a3bb0a7')
    saved_file_path = os.path.join(tmp_path, 'test_loca.loca.xml')
    loca_obj.save_to(saved_file_path)

    loca = tool.convert_xml_to_loca(saved_file_path)
    loca_xml = tool.convert_loca_to_xml(loca)

    loca_obj2 = bg3.bg3_loca_object(loca_xml)
    assert loca_obj2.get('h000006d4gcefbg4092gbb39gfeb27a3bb0a7') is None
    assert loca_obj2.get('haaaa11feg0be5g4f09g978eg030b3e2e62c6') == """Patched Content"""
    assert loca_obj2.get('hfff11ac6ge2f4g4104gbc6fg246521189b73') == """If that's her 'formula' I can smell, it's even fouler than her blood. Gods below..."""

    deleted_content_uids = frozenset(deleted_content_uids)
    i = 0
    for uid in extra_content_uids:
        if uid in deleted_content_uids:
            assert loca_obj2.get(uid) is None
        else:
            assert loca_obj2.get(uid) == "Extra content " + str(i)
        i += 1

