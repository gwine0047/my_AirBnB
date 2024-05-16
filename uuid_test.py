#!/usr/bin/python3
import uuid

id1 = uuid.uuid1()
id3 = uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')
id4 = uuid.uuid4()

print(f'uuid1 = {id1}\nuuid3 = {id3}\nuuid4 = {id4}')