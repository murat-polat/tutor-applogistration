from glob import glob
import os

from .__about__ import __version__

HERE = os.path.abspath(os.path.dirname(__file__))

templates = os.path.join(HERE, "templates")

config = {
    "add": {
        
        "OAUTH2_SECRET": "{{ 24|random_string }}",
    },

    "defaults": {
        "HOST": "{{ LMS_HOST }}:1999",
        "DOCKER_REGISTRY": "{{ DOCKER_REGISTRY }}",
        "DOCKER_IMAGE": "muratp/applogistration",
          }
}

hooks = {

    "init": ["lms","applogistration"],
    "build-image": {"applogistration": "muratp/applogistration"},
    "remote-image": {"applogistration": "muratp/applogistration"},
   
}

def patches():
    all_patches = {}
    for path in glob(os.path.join(HERE, "patches", "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
