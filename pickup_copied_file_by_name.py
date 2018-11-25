# -*- coding: utf-8 -*-

from pathlib import Path
import argparse
import sys
import os
import re

IS_DEBUG = True

def listup_dup(path, p_search_extention):
    files = (file for file in os.listdir(path) if os.path.isfile( os.path.join(path, file) ) )

    photo_files = [file for file in files if p_search_extention.match(file)]

    dup_files = []
    for file in photo_files:
        filename, ext = os.path.splitext(file)
        # extはデフォルトではドットつき！
        ext = ext.replace(".", "")
        # if IS_DEBUG:
        #     #print(filename + "\-[0-9]*" + "\." + ext)
        #     print(file)
        dup_files.extend(  [file for file in photo_files if re.match(filename + "\-[0-9]*" + "\." + ext, file)] )




    dup_files_paths = [os.path.join(path, file) for file in dup_files]


    if args.recursive:
        dires = (d for d in os.listdir(path) if not os.path.isfile( os.path.join(path, d) ) )
        for next_dir_name in dires:
            next_path = os.path.join(path, next_dir_name)
            dup_files_paths.extend( listup_dup(next_path, p_search_extention) )

    return dup_files_paths

    # files = (file for file in os.listdir(path) if os.path.isfile( os.path.join(path, file) ) )

    # photo_files = [file for file in files if p_search_extention.match(file)]

    # probably_duplicated_files = [file for file in photo_files if re.match(".*-[0-9]*.*"  , file)]

    # for file in probably_duplicated_files:
    #     filename, ext = os.path.splitext(file)

    #     # search original file


if __name__ == '__main__':
    # preparing argparse
    parser = argparse.ArgumentParser(description='listup duplicate photos')

    parser.add_argument('arg1', help='target dircotry.')
    parser.add_argument('-r', '--recursive', action="store_true", help='traverse directory recursively.')
    args = parser.parse_args()

    dir_target = args.arg1
    path_dir_target = Path(dir_target)

    # no sensiteve cases
    extensions_tagert = [
        ".*jpeg$",
        ".*JPG$",
        ".*RAF$"
    ]
    st = "|".join(extensions_tagert)
    re_search_extention = re.compile(st, re.IGNORECASE)

    for n in listup_dup(path_dir_target, re_search_extention):
        print(n)






