"""main_template(scriptname) -> scriptfile.

Returns a new script file containing a main funtion template supporting
command options using getopt that's easy to invoke in other contexts.
The code in this script was adapted by Anthony Tarlano from code originally
authored by Guido van Rossum found in his Weblog entry
at http://www.artima.com/weblogs/viewpost.jsp?thread=4829
"""

import os
import sys
import getopt


class Usage(Exception):
    """Catch exception."""

    def __init__(self, msg):
        """Initialize attriutes."""
        self.msg = msg


def main(argv=None):
    """The main function."""
    if argv is None:
        argv = sys.argv
    try:
        if len(argv) != 2:
            raise Usage(__doc__)
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
            raise Usage(msg)

        # option processing
        for option, value in opts:
            if option in ("-h", "--help"):
                raise Usage(__doc__)

        mkscriptfile(args[0])

    except Usage, err:
        print >>sys.stderr, sys.argv[0].split('/')[-1] + ": " \
              + str(err.msg)
        print >>sys.stderr, "\t for help use --help"
        return 2


def mkscriptfile(scriptname):
    """Create template scripte file."""
    os.system('touch ' + scriptname)
    os.system('chmod +x ' + scriptname)

    lines = """#!/usr/bin/env python

# Replace this comment block as a module docstring, the module docstring
# is used as default usage message i.e. raise Usage(__doc__)
# example:
#
# file([file_type]) -> return_values
#
# Returns a ....

import sys
import getopt

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hov:", ["help", "output="])
        except getopt.error, msg:
             raise Usage(msg)

        # option processing
        for option, value in opts:
            if option == "-v":
                verbose = True
            if option in ("-h", "--help"):
                raise Usage(__doc__)
            if option in ("-o", "--output"):
                output = value

    except Usage, err:
        print >>sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >>sys.stderr, "\t for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())"""
    os.system("echo '" + lines + " ' >> " + scriptname)


if __name__ == "__main__":
    sys.exit(main())
