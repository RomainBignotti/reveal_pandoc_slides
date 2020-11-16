#!/usr/bin/env python3

"""
Pandoc filter to process code blocks with class "graphviz" into
graphviz-generated images.

Needs pygraphviz
From : https://github.com/jgm/pandocfilters/
"""

import os
import sys

import pygraphviz

import pandocfilters
from pandocfilters import toJSONFilter, Para, Image, get_filename4code, get_caption, get_extension, get_value

def graphviz(key, value, format, _):
    if key == 'CodeBlock':
        [[ident, classes, keyvals], code] = value
        if "graphviz" in classes:
            caption, typef, keyvals = get_caption(keyvals)
            prog, keyvals = get_value(keyvals, u"prog", u"dot")
            filetype = get_extension(format, "svg", html="svg", latex="pdf")
            dest = get_filename4code("graphviz", code, filetype)

            if not os.path.isfile(dest):
                g = pygraphviz.AGraph(string=code)
                g.layout()
                g.draw(dest, prog=prog)
                sys.stderr.write('Created image ' + dest + '\n')

            return Para([Image([ident, [], keyvals], caption, [dest, typef])])

if __name__ == "__main__":
    toJSONFilter(graphviz)
