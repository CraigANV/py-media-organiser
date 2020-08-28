# Media Organiser

A simple Python app for merging multiple media directories

### config.yml
- sources - a list of source directories
- destination - the directory to copy the files to
- extensions - a list of the file extensions to copy (case-insensitive)

## TODO
- Remove GUID filename component
- Rename file according to EXIF data

## Setup

Use python3 by default
```bash
sudo ln -sf /usr/bin/python3 /usr/bin/python
```

### Conda Setup
```bash
conda env create --file environment.yml
conda env create --file environment.yml --force  # if env already exists
conda activate media-organiser

conda deactivate
conda env remove -n media-organiser
```

## Installing Conda Packages
```bash
conda install -c conda-forge matplotlib
```
