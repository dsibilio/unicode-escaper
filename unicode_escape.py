#!/usr/bin/env python
"""Python script to Unicode escape special characters in an Excel file"""
__author__="Domenico Sibilio"

import string
import openpyxl
import argparse
import os


def escape(str):
    return "".join(map(lambda char: char if char in string.printable else rf"\u{ord(char):04x}", str))


# entrypoint
parser = argparse.ArgumentParser(description='A Python script to Unicode escape special characters in an Excel file')
parser.add_argument('-s', '--source', required=True, help='path to the Excel file to process')
args = parser.parse_args()

source_path = args.source

source_workbook = openpyxl.load_workbook(source_path)

for sheet in source_workbook.worksheets:
    for row in sheet.iter_rows():
        for cell in row:
            cell.value = escape(cell.value)

target_path = os.path.basename(source_path)
source_workbook.save(target_path)
print(f'Generated: {target_path}')