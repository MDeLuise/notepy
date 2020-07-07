#!/usr/bin/env python3

import sys
from notepy import Notepy

from plugin.Scrollbar import ScrollbarPlugin
from plugin.TextLineNumber import TextLineNumberPlugin
from plugin.Menu import MenuPlugin
from plugin.FileHandler import FileHandlerPlugin
from plugin.TextSelection import TextSelectionPlugin
from plugin.RightClick import RightClickPlugin
from plugin.FindAndReplace import FindReplacePlugin




def start_app(pos=None):
    plugins = [
        ScrollbarPlugin,
        TextLineNumberPlugin,
        MenuPlugin,
        FileHandlerPlugin,
        TextSelectionPlugin,
        RightClickPlugin,
        FindReplacePlugin
    ]

    app = Notepy(plugins=plugins, pos=pos)

    #if len(sys.argv) > 2 and FileHandlerPlugin in plugins:
    #    print("TODO")




if (__name__ == "__main__"):
    if "-t" not in sys.argv:
        start_app()
    else:
        start_app((sys.argv[2], sys.argv[3]))
