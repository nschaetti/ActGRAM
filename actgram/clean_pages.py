#
# This file is part of the XXX distribution (https://github.com/nschaetti/ActGRAM).
# Copyright (c) 2022 Nils Schaetti.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Copyright Nils Schaetti <n.schaetti@gmail.com>

# Imports
import os
import sys
import re
import argparse

# Command
parser = argparse.ArgumentParser(prog="clean_pages")
parser.add_argument("-t", "--text", type=str, required=True)
parser.add_argument("-o", "--output", type=str, required=True)
args = parser.parse_args()

# Read all text
with open(args.text, 'r') as in_file:
    # Read text
    input_text = in_file.read()

    # Search matches
    matches = re.findall(r"[\r\n|\r|\n]{2,}([0-9]+)\s{1}[\r\n|\r|\n]{3,}", input_text)

    # Print number of matches
    print(f"{len(matches)} matches")

    # First page
    page_number = int(matches[0]) - 1

    # For each match
    for m_i, m in enumerate(matches):
        # Check page number
        if int(m) != page_number + 1:
            print(f"ERROR: invalid page number: old {page_number}, current {int(m)}")
        else:
            # print(f"Page {int(m)}")
            pass
        # end if

        # String to replace
        str_to_replace = ''.join(['\n']*2)
        str_to_replace += m
        str_to_replace += ''.join(['\n'] * 3)

        # Replace
        input_text = input_text.replace(str_to_replace, "")

        # New page number
        page_number = int(m)
    # end for
# end with

# Write output
with open(args.output, 'w') as out_file:
    out_file.write(input_text)
# end with
