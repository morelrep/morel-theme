import shutil
import os
import sys

folders_to_copy = [
    '_abouts',
    '_authors',
    '_books',
    '_chriterias',
    '_cities',
    '_data',
    '_posts',
    '_publishers',
    '_repositories',
    'assets',
    '_includes',
    'img'
]

files_to_copy = [
    'config.yml',
    'about.md',
    'add.md',
    'books.md',
    'downloads.md',
    'index.html',
    'no-downloads.md',
    'podcast.md',
    'search.html',
    'translations.md'
]

destination_folder = './assets/source'

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Get the parent directory path
parent_dir = os.path.abspath(os.path.join(sys.path[0], '../../../../'))

# Copy folders
for folder in folders_to_copy:
    source = os.path.join(parent_dir, folder)
    destination = os.path.join(destination_folder, folder)
    shutil.copytree(source, destination)

# Copy files
for file in files_to_copy:
    source = os.path.join(parent_dir, file)
    destination = os.path.join(destination_folder, file)
    shutil.copy(source, destination)

print('Folders and files copied successfully.')
