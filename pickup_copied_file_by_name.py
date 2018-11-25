# -*- coding: utf-8 -*-

from pathlib import Path
import argparse
import sys
import os
import re

def listup_dup(path, target_extentions, do_recursive):
    target_extentions_regexp = [(".*" + item + "$") for item in target_extentions]
    # insensiteve case
    p_search_extention = re.compile("|".join(target_extentions_regexp), re.IGNORECASE)

    files = (file for file in os.listdir(path) if os.path.isfile( os.path.join(path, file) ) )

    photo_files = [file for file in files if p_search_extention.match(file)]

    dup_files = []
    for file in photo_files:
        filename, ext = os.path.splitext(file)
        # extはデフォルトではドットつき！
        ext = ext.replace(".", "")

        dup_files.extend(  [file for file in photo_files if re.match(filename + "\-[0-9]*" + "\." + ext, file)] )

    dup_files_paths = [os.path.join(path, file) for file in dup_files]

    if do_recursive:
        dires = (d for d in os.listdir(path) if not os.path.isfile( os.path.join(path, d) ) )
        for next_dir_name in dires:
            next_path = os.path.join(path, next_dir_name)
            dup_files_paths.extend( listup_dup(next_path, target_extentions, do_recursive) )

    return dup_files_paths


if __name__ == '__main__':
    # preparing argparse
    parser = argparse.ArgumentParser(description='listup duplicate photos')

    parser.add_argument('arg1', help='target dircotry.')
    parser.add_argument('-r', '--recursive', action="store_true", help='traverse directory recursively.')
    parser.add_argument('-e', '--extension_list', nargs='+', default=[], help='target extentions.')
    parser.add_argument('--debug', action="store_true", help='enable debug mode.')
    args = parser.parse_args()

    dir_target = args.arg1
    path_dir_target = Path(dir_target)

    extensions_tagert = [
        "jpeg",
        "JPG",
        "RAF"
    ]

    extensions_tagert.extend(args.extension_list)

    # st = "|".join(extensions_tagert)
    # re_search_extention = re.compile(st, re.IGNORECASE)

    for n in listup_dup(path_dir_target, extensions_tagert, args.debug):
        print(n)






