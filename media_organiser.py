#!/usr/bin/env python3

import glob
import uuid
import os
import yaml


def get_stem_and_extension(filepath):
    """Return the filename and extension separately"""
    extension = os.path.splitext(filepath)[1]
    filename = os.path.split(filepath)[1]
    stem = os.path.splitext(filename)[0]

    return stem, extension


def insert_uid(filepath):
    """Return the filename with a random UID inserted before the extension"""
    stem, extension = get_stem_and_extension(filepath)
    uid = uuid.uuid1().hex[:8]
    uid_filename = stem + '_' + uid + extension
    return uid_filename


def insensitive_glob(pattern):
    """Return list of filepaths matching the pattern"""

    def either(c):
        return '[%s%s]' % (c.lower(), c.upper()) if c.isalpha() else c

    return glob.glob(''.join(map(either, pattern)), recursive=True)


def main():
    with open(r'config.yml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        sources = config['sources']
        destination = config['destination']
        extensions = config['extensions']

        print("Source dirs: ", sources)
        print("Destination dir: ", destination)

        source_files = []

        for source_dir in sources:
            print("Scanning: ", source_dir)

            for extension in extensions:
                files = insensitive_glob(source_dir + '/**/*.' + extension)
                source_files += files

        print('\n'.join(source_files))
        print(len(source_files))

        print(insert_uid(source_files[0]))


if __name__ == "__main__":
    main()
