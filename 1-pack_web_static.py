#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder of AirBnB Clone repo
"""
from fabric.api import local
import datetime
from fabric.decorators import runs_once


@runs_once
def do_pack():
    """
    Creates a timestamped .tgz archive
    of the files in the web_static folder.
    """

    local("mkdir -p versions")

    now = datetime.datetime.now()
    archive_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    directory = "web_static"
    path = "versions/{}".format(archive_name)

    result = local("tar -czvf {} {}".format(
             path, directory), capture=True)

    if result.failed:
        return None
    else:
        return path
