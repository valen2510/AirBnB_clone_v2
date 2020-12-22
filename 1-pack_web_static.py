#!/usr/bin/python3
""" Function do_pack that generates a .tgz archive
    from the contents of the web_static
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Function to generate a tgz from web_static"""
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        tgz_file = "versions/web_static_{}.tgz".format(date)
        local("tar -czvf {} web_static".format(tgz_file))
        return tgz_file
    except:
        return None
