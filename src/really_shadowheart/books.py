from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files
from .flags import *

############################################################################
# This puts back the original version of Druid Notebook from EA
############################################################################

def patch_druid_notebook() -> None:
    f = files.get_file('Gustav', 'Mods/Gustav/Localization/Act1_Books.lsf')
    books = f.xml.findall('./region[@id="TranslatedStringKeys"]/node[@id="TranslatedStringKeys"]/children/node[@id="TranslatedStringKey"]')
    for book in books:
        book_uuid = bg3.get_bg3_attribute(book, 'UUID')
        if book_uuid is None:
            continue
        if book_uuid == 'DEN_DruidLair_SharTempleResearch':
            bg3.set_bg3_attribute(book, 'Content', 'hbb1bd14dg56f9g40f3g8ee9gb7353e6d6d04', attribute_type = 'TranslatedString', version = 1)
            return

add_build_procedure('patch_druid_notebook', patch_druid_notebook)
