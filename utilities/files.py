from uuid import uuid4
import os


def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)
    return name, ext


def upload_file(file, to):
    name, ext = get_filename_ext(file)
    random_str = uuid4()
    return f"{to}/{random_str}{ext}"
