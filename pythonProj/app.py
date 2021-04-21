#!/usr/bin/env python3

# **********************************************************************************
# Title:      Code Analysis and Transformation Based on Regulated Grammars
# Author:     Matúš Arbet
# Supervisor: Meduna Alexander, prof. RNDr., CSc., UIFS FIT VUT
# **********************************************************************************

import parseArg
import sys


def main(argv):
    """This is main function of application.

    :param argv: List of command-line arguments.
    :type argv: List
    """
    parseArg.parseArgs(argv)


if __name__ == "__main__":
    main(sys.argv[1:])
