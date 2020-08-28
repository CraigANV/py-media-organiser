#!/usr/bin/env python3

import glob
import yaml


def main():
    with open(r'config.yml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        sources = config['sources']
        destination = config['destination']
        print(config)
        print(sources)
        print(destination)

        source_files = []

        for source_dir in sources:
            print("Scanning: ", source_dir)
            files = glob.glob(source_dir + '/**/*.mp4', recursive=True)
            print('\n'.join(files))
            source_files += files

        print('\n'.join(source_files))
        print(len(source_files))


if __name__ == "__main__":
    main()
