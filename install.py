#!/usr/bin/env python3

import os
import argparse
import pwd, grp

def installConfig(config, dest, commentStart='#', uid=-1, gid=-1):
  beginTag = commentStart + ' Automatic config installer section BEGIN'
  endTag   = commentStart + ' Automatic config installer section END'
  with open(config) as f:
    configLines = f.read().splitlines()
  if not os.path.isfile(dest):
    resultLines = [beginTag] + configLines + [endTag]
  else:
    with open(dest) as f:
      destLines = f.read().splitlines()
    resultLines = []
    skip = False
    for line in destLines:
      if line == beginTag:
        skip = True
      if not skip:
        resultLines.append(line)
      if line == endTag:
        skip = False
    resultLines += [beginTag] + configLines + [endTag]
  with open(dest, 'w') as f:
    for line in resultLines:
      print(line, file=f)
  os.chown(dest, uid, gid)

def main():
  parser = argparse.ArgumentParser(description='Configs installer')
  parser.add_argument('-u', '--user', required=True, help='Username of user to install configs for')
  parser.add_argument('-g', '--group', required=True, help='Username of user to install configs for')
  cli_args = parser.parse_args()
  home = os.path.expanduser('~%s' % cli_args.user)

  def installHomeConfig(*args, **kwargs):
    uid = pwd.getpwnam(cli_args.user).pw_uid
    gid = grp.getgrnam(cli_args.group).gr_gid
    installConfig(*args, uid=uid, gid=gid, **kwargs)

  installHomeConfig('vimrc', os.path.join(home, '.vimrc'), commentStart='"')
  installHomeConfig('tmux.conf', os.path.join(home, '.tmux.conf'))
  installHomeConfig('bashrc', os.path.join(home, '.bashrc'))

  installConfig('inputrc', '/etc/inputrc')


if __name__ == "__main__":
  main()
