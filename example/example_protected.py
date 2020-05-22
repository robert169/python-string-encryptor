import base64
a = (base64.b64decode(b'cm9iZXJ0').decode('utf-8'))
if a != (base64.b64decode(b'cHl0aG9u').decode('utf-8')):
    print((base64.b64decode(b'VHJ1ZQ==').decode("utf-8")))
else:
    print((base64.b64decode(b'RmFsc2U=').decode("utf-8")))

b = (base64.b64decode(b'cm9iZXJ0').decode('utf-8'))
if b == ((base64.b64decode(b'cm8=').decode('utf-8'))+(base64.b64decode(b'YmVydA==').decode('utf-8'))):
    print((base64.b64decode(b'VHJ1ZQ==').decode("utf-8")))
