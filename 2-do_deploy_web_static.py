#!/usr/bin/python3
"""Create and distribute an archive to the servers,
    using function deploy
"""
from fabric.api import put, run, env
from os import path

env.user = 'ubuntu'
env.hosts = ['35.229.108.96', '35.196.60.22']


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
