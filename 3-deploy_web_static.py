#!/usr/bin/python3
""" Function that do a full deployment of static content into servers
"""

from fabric.api import local, env, put, run
from datetime import datetime
from os import path

env.user = 'ubuntu'
env.hosts = ['35.229.108.96', '35.196.60.22']


def deploy():
    """Function that do a full deployment"""
    web_static_pack = do_pack()

    if web_static_pack is None:
        return False
    return do_deploy(web_static_pack)


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


def do_deploy(archive_path):
    """function to deploy an archive to the servers"""
    if path.exists(archive_path) is False:
        return False

    archive = archive_path.split('/')[1]
    folder = archive[:-4]

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(folder))
        run("tar -xzf /tmp/{} -C \
            /data/web_static/releases/{}".format(archive, folder))
        run("rm /tmp/{}".format(archive))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}".format(folder, folder))
        run("rm -rf /data/web_static/releases/{}/web_static".format(folder))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} \
            /data/web_static/current".format(folder))
        print('New release deployed!')
        return True
    except:
        return False
