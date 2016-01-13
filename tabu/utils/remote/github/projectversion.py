# -*- coding: utf-8 -*-

from simplygithub.authentication import profile
from simplygithub import branches, files


def get_profile(name):
    prof = profile.read_profile(name)
    return prof


def write_profile(name, repo, token):
    prof = profile.write_profile(name, repo, token)
    return prof


def get_version_file(profile):
    data = files.list_files(profile, "master")
    return data
