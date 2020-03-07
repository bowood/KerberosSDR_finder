#!/usr/bin/python

import sys, json

myjson = json.load(sys.stdin)

result = {
  'success':'true',
  'message':'The Command Completed Successfully',
}

with open('/home2/greenim9/data/data.json', 'w') as f:
    json.dump(myjson, f, ensure_ascii=False, indent=4)

print 'Content-Type: application/json\n\n'
print json.dump(result, sys.stdout)
print json.dump(myjson, sys.stdout)



