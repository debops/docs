# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 DebOps Project http://debops.org/

import os
import fnmatch
import re
from subprocess import check_output

import yaml2rst


def yaml2rst_role_defaults(dir_path):  # NOQA
    """Generate documentation on the fly based on Ansible default variables"""
    for element in os.listdir(dir_path):
        if os.path.isdir(dir_path + element) and element not in ['includes']:
            yaml2rst.convert_file(
                dir_path + element + '/defaults/main.yml',
                dir_path + element + '/docs/defaults.rst',
                strip_regex=r'\s*(:?\[{3}|\]{3})\d?$',
                yaml_strip_regex=r'^\s{66,67}#\s\]{3}\d?$',
            )


# Fix "Edit on GitHub" links (((
# Jinja2 Support is only basic Jinja2 without all the good stuff from Ansible. So I am not gonna mess with that or try to extend it as in:
# https://stackoverflow.com/questions/36019670/removing-the-edit-on-github-link-when-using-read-the-docs-sphinx-with-readthed
# What I am gonna do instead is just recompute source file to URL map in Python and job done.
#
# git_repo.iter_submodules() fails with "unknown encoding: -----BEGIN PGP SIGNATURE-----"
#
# https://stackoverflow.com/a/21909382
#  import sphinx.application.TemplateBridge

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


def get_source_file_to_url_map(start_dir='.', skip_patterns=[]):
    source_file_to_url_map = {}
    repo_dir_to_url_map = {}
    list_of_submod_paths = []

    cur_dir = os.path.abspath(os.path.dirname(__file__))

    for submodule_path in check_output(['git', 'submodule', '--quiet', 'foreach', 'pwd']).split('\n'):
        if submodule_path.startswith(cur_dir):
            submodule_path = submodule_path[len(cur_dir):].lstrip('/')
        list_of_submod_paths.append(submodule_path)

    for source_file_name in find_files('.', '*.rst'):
        pagename_source_file = source_file_name.lstrip('/.')

        skip = False
        for skip_pattern in skip_patterns:
            if re.search(skip_pattern, pagename_source_file):
                #  print(pagename_source_file)
                skip = True
                break

        if skip:
            continue

        dir_path = os.path.dirname(source_file_name)
        if len(dir_path) > 2:
            dir_path = dir_path.lstrip('/.')

        # Can also contain subdirs in a repo but this optimization should already
        # get factor 10 in performance for git Invokation.
        if dir_path not in repo_dir_to_url_map:
            #  git_repo = git.Repo(dir_path)
            #  repo_dir_to_url_map[dir_path] = git_repo.remotes.origin.url
            for remote_line in check_output(['git', '-C', dir_path, 'remote', '-v']).split('\n'):
                remote_item = re.split(r'\s', remote_line)
                if remote_item[0] == 'origin' and remote_item[2] == '(fetch)':
                    base_url = remote_item[1]
                    if base_url.endswith('.git'):
                        base_url = base_url[:-4]
                    repo_dir_to_url_map[dir_path] = base_url
                    #  print(repo_dir_to_url_map[dir_path])

        relative_pagename = pagename_source_file

        if relative_pagename in ['index.rst', 'ansible/roles/index.rst']:
            relative_pagename = 'docs/' + relative_pagename

        for submod_path in list_of_submod_paths:
            if pagename_source_file.startswith(submod_path + '/'):
                relative_pagename = pagename_source_file[len(submod_path):].lstrip('/')

        # Does not work for legacy roles yet. Disabled.
        #  if re.match(r'docs/copyright(?:\.rst)$', relative_pagename, flags=re.I):
        #      relative_pagename = 'COPYRIGHT'

        if re.match(r'docs/readme(?:\.rst)$', relative_pagename, flags=re.I):
            relative_pagename = 'README.rst'

        if re.match(r'docs/changelog(?:\.rst)$', relative_pagename, flags=re.I):
            relative_pagename = 'CHANGES.rst'

        pagename_source_file = re.sub(r'\.rst$', '', pagename_source_file)
        print(dir_path)
        source_file_to_url_map[pagename_source_file] = {
            'url': repo_dir_to_url_map[dir_path],
            'pagename': relative_pagename,
        }
        #  print('{}: {}'.format(pagename_source_file, source_file_to_url_map[pagename_source_file]))

    #  print(source_file_to_url_map)
    #  import pprint
    #  pprint.pprint(source_file_to_url_map)
    return source_file_to_url_map
