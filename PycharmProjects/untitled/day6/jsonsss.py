#!/usr/bin/env python
#-*- coding: utf-8 -*-
s = '{"desc":"ubndsjds","status":1002}'
l = "[12,11,14,5]"
import json
result = json.loads(l)
print(result, type(result))