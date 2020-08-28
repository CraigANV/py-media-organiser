#!/usr/bin/env python3

import glob
import uuid
import os
from shutil import copyfile
import hashlib
from pathlib import Path
import yaml


def get_stem_and_extension(file_path):
    """Return the filename and extension separately"""
    extension = os.path.splitext(file_path)[1]
    filename = os.path.split(file_path)[1]
    stem = os.path.splitext(filename)[0]

    return stem, extension


def insert_uid(file_path):
    """Return the filename with a random UID inserted before the extension"""
    stem, extension = get_stem_and_extension(file_path)
    uid = uuid.uuid1().hex[:8]
    uid_filename = stem + '_' + uid + extension
    return uid_filename


def insensitive_glob(pattern):
    """Return list of file paths matching the pattern"""

    def either(c):
        return '[%s%s]' % (c.lower(), c.upper()) if c.isalpha() else c

    return glob.glob(''.join(map(either, pattern)), recursive=True)


def get_source_files(source_dirs, extensions):
    """Returns a list of all files in a directory and subdirectories that match one of the extensions"""
    source_files = []
    for source_dir in source_dirs:
        print("Scanning: ", source_dir)

        for extension in extensions:
            files = insensitive_glob(source_dir + '/**/*.' + extension)
            source_files += files
    return source_files


def get_file_hash(file_path):
    """Returns an MD5 hash of the input file"""
    with open(file_path, 'rb') as input_file:
        data = input_file.read()
    file_hash = hashlib.md5(data).hexdigest()
    return file_hash


def get_existing_hashes(directory, extensions):
    """
    Returns a list of MD5 hashes of all files with matching extensions in the destination directory
    and subdirectories

    :param directory: The directory to process
    :param extensions: A list of extensions to generate hashes for
    :return: A list of MD5 hashes
    """
    existing_files = []
    for extension in extensions:
        files = insensitive_glob(directory + '/**/*.' + extension)
        existing_files += files

    existing_hashes = []
    for file in existing_files:
        file_hash = get_file_hash(file)
        existing_hashes.append(file_hash)

    return existing_hashes


def copy_new_files(source_dirs, destination_dir, extensions):
    """
    Copies files from sources and their subdirectories to a flat structure in destination.
    Only files that match (case-insensitive) on of the extensions are processed.
    Files that already exist in destination are skipped

    :param source_dirs: A list of directories to process
    :param destination_dir: The target directory where files will be cloned to
    :param extensions: A list of file extensions to process
    """
    source_files = get_source_files(source_dirs, extensions)

    existing_hashes = get_existing_hashes(destination_dir, extensions)

    for file in source_files:
        file_hash = get_file_hash(file)

        if file_hash in existing_hashes:
            print("File already exists: ", file)
            continue

        destination_file = destination_dir + insert_uid(file)

        print("Copying " + file + " to " + destination_file)
        copyfile(file, destination_file)
        existing_hashes.append(file_hash)


def main():
    with open(r'config.yml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        source_dirs = config['sources']
        destination_dir = os.path.join(config['destination'], '')  # adds trailing slash if not present
        extensions = config['extensions']

    print("Source dirs: ", source_dirs)
    print("Destination dir: ", destination_dir)
    print("Extensions: ", extensions)

    Path(destination_dir).mkdir(parents=True, exist_ok=True)

    copy_new_files(source_dirs, destination_dir, extensions)


if __name__ == "__main__":
    main()
