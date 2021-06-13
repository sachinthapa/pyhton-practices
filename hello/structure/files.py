import pathlib
        
def unique_path(directory, name_pattern):
    """Find a path name that does not already exist"""
    counter = 0
    while True:
        counter += 1
        path = directory / name_pattern.format(counter)
        if not path.exists():
            print(f'unique_path= {path}')
            return path

def add_empty_file(path):
    """Create an empty file at the given path"""
#    print(f"Create file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch()

argvs_path = '/home/itnepal/django-apps/pytpractical/src/hello'; #pathlib.Path.cwd()
root = pathlib.Path(argvs_path).resolve()

unique_path = unique_path(root, "{:03d}")


for path in root.rglob("*"):
#    print(path)
    if path.is_file() and  unique_path not in path.parents:
        #print(f'path parent {path.parent}')
        rel_path = path.relative_to(root)
        print(rel_path)
        add_empty_file(unique_path / rel_path)
