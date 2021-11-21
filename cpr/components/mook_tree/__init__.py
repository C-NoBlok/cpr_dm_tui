import json
from pathlib import Path

from cpr.mooks.mook import Mook


def load_custom_mooks():
    usr_data_folder = Path.home() / '.cpr'
    if not usr_data_folder.exists():
        usr_data_folder.mkdir()
    custom_mook_files = usr_data_folder.glob('*.mook')

    custom_mooks = []
    for custom_mook_file in custom_mook_files:
        with open(custom_mook_file, 'r') as f:
            custom_mook = json.load(f)
        custom_mooks.append(Mook.from_dict(custom_mook))
    return custom_mooks

