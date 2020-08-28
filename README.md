# Media Organiser

A simple Python app for merging multiple photo / image backup directories

## TODO
- Insert GUID into filenames to prevent collisions
- Copy files to common directory
- Sort through and remove dupes
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
