import base64
import os, sys
strings_protected = 0
try:
    main_file = (sys.argv[1])
    if ((sys.argv[1].split('\\')[-1]))[-3:] == ".py":
        pass
    else:
        print('Make sure this file in made in python and contain extension .py')
        input()
        os._exit(0)
except:
    print('Drag and drop file that you want to protect')
    input()
    os._exit(0)
second_file = (sys.argv[1].split('\\')[-1]).replace('.py', '')
lol = 0
with open(main_file, "r") as m:
    with open(second_file+"_protected.py", "w") as n:
        n.write('import base64\n')
        for a in m:
            lol += 1
            try:
                if '"""' in a or "'''" in a:
                    n.write(a)
                else:
                    l1x = ['f"', 'b"', 'u"', 'r"', 'fr"', 'rf"', 'fr"', 'rb"', 'br"', "f'", "b'", "u'", "r'", "fr'", "rf'", "fr'", "rb'", "br'"]
                    if any(n in a for n in l1x):
                        n.write(a)
                    else:
                        if a.count('"') == 0:
                            if a.count("'") == 0:
                                n.write(a)
                            else:
                                l = {}
                                for each in range(int(a.count("'")) // 2):
                                    if each == 0:
                                        b = a.split("'")[each+1]
                                        strings_protected += 1
                                    else:
                                        if (each % 2) == 0:
                                            b = a.split("'")[each+1]
                                        else:
                                            b = a.split("'")[each+2]
                                        strings_protected += 1
                                    base64_bytes = base64.b64encode(bytes(b,'utf-8'))
                                    l[f"'{b}'"] = f'(base64.b64decode({base64_bytes}).decode("utf-8"))'
                                    print(f'[INFO] Protected line number {lol}')
                                    
                                for each in l:
                                    a = a.replace(f'{each}', f'{l[each]}')
                                n.write(a)
                        else:
                            l = {}
                            for each in range(int(a.count('"')) // 2):
                                if each == 0:
                                    b = a.split('"')[each+1]
                                    strings_protected += 1
                                else:
                                    if (each % 2) == 0:
                                        b = a.split('"')[each+1]
                                    else:
                                        b = a.split('"')[each+2]
                                    strings_protected += 1
                                base64_bytes = base64.b64encode(bytes(b,'utf-8'))
                                print(f'[INFO] Protected line number {lol}')
                                l[f'"{b}"'] = f"(base64.b64decode({base64_bytes}).decode('utf-8'))"
                                
                            for each in l:
                                a = a.replace(f'{each}', f'{l[each]}')
                            n.write(a)
                        
            except Exception as e:
                n.write(a)
print('Protected {0} strings'.format(strings_protected))
print(f'File saved as: {second_file+"_protected.py"}')
print('Done')
input()
os._exit(0)
