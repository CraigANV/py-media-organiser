#!/usr/bin/env python3

import yaml


def main():
    with open(r'config.yml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        sources = config['sources']
        destination = config['destination']
        print(config)
        print(sources)
        print(destination)


if __name__ == "__main__":
    main()
