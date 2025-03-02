import os, shutil

def copy_directory(source_path, destination_path):
    if not os.path.exists(source_path):
        raise ValueError(f"Source path {source_path} doesn't exist")

    dirlist = os.listdir(source_path)

    if os.path.exists(destination_path):
        print(f"Destination path {destination_path} exists, deleting contents...")
        shutil.rmtree(destination_path)
    else:
        print(f"Destination path {destination_path} does not exist, creating...")

    os.mkdir(destination_path)

    for filename in dirlist:
        from_path = os.path.join(source_path, filename)
        to_path = os.path.join(destination_path, filename)
        if os.path.isfile(from_path):
            print(f"Copying {from_path} to {to_path}")
            shutil.copy(from_path, to_path)
        else:
            copy_directory(from_path, to_path)