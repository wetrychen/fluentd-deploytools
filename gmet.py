#!/usr/local/bin/env python

import sys,os,re
import shutil
import configparser

#config fluentd
indexname = sys.argv[1]

yw = indexname.split('_')[0]
mo = indexname.split('_')[1]
detail = indexname.split('_')[2]

try:
  shutil.copy2('fluentd.template.conf',indexname + '.conf')

  f = open(indexname + '.conf','r+')
  all_lines = f.readlines()
  f.seek(0)
  f.truncate()

  for line in all_lines:
    line = line.replace('bu_module_logtype', indexname)
    line = line.replace('bu.module.logtype', yw + '.' + mo + '.' + detail)
    f.write(line)
  f.close()

  f2 = open('td-agent.conf', 'a')
  content = '\n'"@include %s.conf" %(indexname)
  f2.write(content)
  f2.close()

except Exception, e:
  print str(e)
os.system('/etc/init.d/td-agent restart')
