"""Creation of directory tree"""
from pathlib import Path

# prefix components:
SPACE =  '    '
BRANCH = '│   '
# pointers:
TREE =    '├── '
LAST =   '└── '

""" function for directory tree"""
def tree(dir_path: Path, prefix: str=''):
    """directory tree"""
    contents = list(dir_path.iterdir())
    # contents each get pointers that are ├── with a final └── :
    pointers = [TREE] * (len(contents) - 1) + [LAST]
    for pointer, path in zip(pointers, contents):
        yield prefix + pointer + path.name
        if path.is_dir():
            extension = BRANCH if pointer == TREE else SPACE
            # i.e. space because last, └── , above so no more |
            yield from tree(path, prefix=prefix+extension)

for line in tree(Path.home() / 'floyd'):
    print(line)
