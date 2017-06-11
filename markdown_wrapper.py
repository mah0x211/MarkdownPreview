from __future__ import absolute_import
import sublime
import traceback

from markdown import Markdown, util
from markdown.extensions import Extension
import importlib


class StMarkdown(Markdown):
    def __init__(self, *args, **kwargs):
        Markdown.__init__(self, *args, **kwargs)
        self.Meta = {}

    def registerExtensions(self, extensions, configs):
        """
        Register extensions with this instance of Markdown.

        Keyword arguments:

        * extensions: A list of extensions, which can either
           be strings or objects.  See the docstring on Markdown.
        * configs: A dictionary mapping module names to config options.

        """
        for ext in extensions:
            try:
                # Make sure we aren't using old form `extension(option=value)`
                if isinstance(ext, util.string_type) and ('(' not in ext):
                    ext = self.build_extension(ext, configs.get(ext, []))
                if isinstance(ext, Extension):
                    ext.extendMarkdown(self, globals())
                elif ext is not None:
                    raise TypeError(
                        'Extension "%s.%s" must be of type: "markdown.Extension"'
                        % (ext.__class__.__module__, ext.__class__.__name__))
            except:
                print(str(traceback.format_exc()))

        return self
