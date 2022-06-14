# Importing Necessary Modules

from marshal import dumps
from binascii import hexlify
from random import randint, shuffle
from pystyle import *

# Initialise Frontend

banner1 = r'''
  ██████  ██▓███  ▓█████  ▄████▄  ▄▄▄█████▓▓█████  ██▀███               
▒██    ▒ ▓██░  ██▒▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒             
░ ▓██▄   ▓██░ ██▓▒▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒             
  ▒   ██▒▒██▄█▓▒ ▒▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄               
▒██████▒▒▒██▒ ░  ░░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒             
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░             
░ ░▒  ░ ░░▒ ░      ░ ░  ░  ░  ▒       ░     ░ ░  ░  ░▒ ░ ▒░             
░  ░  ░  ░░          ░   ░          ░         ░     ░░   ░              
      ░              ░  ░░ ░                  ░  ░   ░                  
                         ░'''[1:]

banner2 = r"""
                            ,-.                               
       ___,---.__          /'|`\          __,---,___        
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.     
  ,'        |           ~'\     /`~           |        `.    
 /      ___//              `. ,'          ,  , \___      \  
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |  
|   /          /\_  `   .    |    ,      _/\          \   | 
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
 \  \           | `._   `\\  |  //'   _,' |           /  /    
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'   
     ``       /     \    ,='/ \`=.    /     \       ''        
             |__   /|\_,--.,-.--,--._/|\   __|                
             /  `./  \\`\ |  |  | /,//' \,'  \                
            /   /     ||--+--|--+-/-|     \   \               
           |   |     /'\_\_\ | /_/_/`\     |   |              
            \   \__, \_     `~'     _/ .__/   /            
             `-._,-'   `-._______,-'   `-._,-'"""[1:]

banner = Add.Add(banner1, banner2, center=True)
purple = Col.StaticMIX([Col.blue, Col.purple])

def stage(text: str, symbol: str = '...') -> str:
    ppurple = purple if symbol == '...' else Col.light_blue
    return f""" {Col.Symbol(symbol, ppurple, Col.blue)} {ppurple}{text}{Col.reset}"""

# Initialise Backend

class Specter:

    vars = []
    
    # Execute obfuscation system

    def specterize(script: str) -> str:
        print(stage("Specterizing!", "#"))
        script = Specter.anti_skid(script=script)
        print('\n')
        print(stage("Applying Security patches [1/3]", ">"))
        script = Specter.layer_1(script=script)
        print('\n')
        print(stage("Applying Security patches [2/3]", ">"))
        script = Specter.layer_2(script=script)
        print('\n')
        print(stage("Applying Security patches [3/3]", ">"))
        script = Specter.layer_3(script=script)
        print('\n')
        return script

    # Security func: Convert values to hex

    def hex(text: str) -> bytes:
        return "b'" + "".join(fr"\x{hexlify(t.encode('utf-8')).decode()}" for t in text) + "'"

    # Security func: Encrypt values

    def encrypt(text: str, key: int) -> str:
        return "\x00".join(str(ord(x)+key) for x in text)

    # Security func: Randomize variables

    def randvar() -> str:
        var = randint(1000, 9999)
        while var in Specter.vars:
            var = randint(1000, 9999)
        Specter.vars.append(var)
        return f"__{var}__"
    
    # Get value of key

    def get_key_by_value(vars, key) -> str:
        return list(vars.keys())[list(vars.values()).index(key)]

    # Anti-skid system

    def anti_skid(script: str) -> str:
        return r"""
# This is an de-obfuscated code
# Specter: billythegoat356
# Github: https://github.com/billythegoat356/Specter
# Discord: https://discord.gg/plague

try:
    if (
        __author__ != "billythegoat356" or
        __github__ != "https://github.com/billythegoat356/Specter" or
        __discord__ != "https://discord.gg/plague" or
        __license__ != "EPL-2.0" or
        __code__ != "Hello world!" or
        "Specter" not in globals() or
        "Func" not in globals()
    ):
        int('skid')
except:
    input("You just executed a file obfuscated with Specter!\n\nAuthor: billythegoat356\nGitHub: https://github.com/billythegoat356/Specter\nDiscord: https://discord.gg/plague")
    __import__('sys').exit()    

"""[1:] + script

    # Layer 1: Randomize values

    def layer_1(script: str) -> str:
        ten_split = []
        key = randint(3, 33)
        splitting = randint(3, 9)
        while True:
            if len(script) >= splitting:
                ten_split.append(Specter.hex(Specter.encrypt(script[:splitting], key)))
                script = script[splitting:]
            else:
                ten_split.append(Specter.hex(Specter.encrypt(script, key)))
                break
        lexec = Specter.hex(Specter.encrypt("exec", key))
        lkey = Specter.hex(str(key))
        ten_split.append(lexec)
        ten_split.append(lkey)
        ten_split.append("globals")
        correct = [x for x in ten_split]
        shuffle(ten_split)
        vars = {Specter.randvar(): x for x in ten_split}
        script = ",".join(vars.keys()) + '=' + ",".join(vars.values()) + '\n'
        all_correct = []
        for x in correct:
            if x not in (lexec, lkey, "globals"):
                all_correct.append(Specter.get_key_by_value(vars, x))
        l1, l2, l3 = Specter.randvar(), Specter.randvar(), Specter.randvar()
        glob = f"{Specter.get_key_by_value(vars, 'globals')}()[{l1}({l2}={Specter.get_key_by_value(vars, lexec)})]"
        print(stage("Randomizing keys"))
        lambdas = [fr"{l1}=lambda {l2}:''.join(chr(int({l3})-int({lkey}))for {l3} in {l2}.decode().split('\x00'))",
                   f"(lambda {l3}:{glob}(''.join({l1}({l2}={l2})for {l2} in {l3}),{Specter.get_key_by_value(vars, 'globals')}()))([{','.join(all_correct)}])",]
        script = "from builtins import *\n" + script + '\n'.join(lambdas)
        return script

    # Layer 2: Compile and dump Script

    def layer_2(script: str) -> str:
        print(stage("Compiling and dumping"))
        return dumps(compile(script, 'Specter', 'exec'))

    # Layer 3: Camoflate Script

    def layer_3(script: str) -> str:
        split = []
        splitting = 2000
        while True:
            if len(script) >= splitting:
                split.append(script[:splitting])
                script = script[splitting:]
            else:
                split.append(script)
                break
        vars = {Specter.randvar(): x for x in split}
        codevars = "\n".join(f"{a} = Func.calculate({randint(1,9)}){' ' * 500},Func.define('{a}', {b})" for a, b in vars.items())
        print(stage("Camoflating script"))
        script = fr"""
# This is a specterized file.
# Specter: billythegoat356
# Github: https://github.com/billythegoat356/Specter
# Discord: https://discord.gg/plague

__author__ = "billythegoat356"
__github__ = "https://github.com/billythegoat356/Specter"
__discord__ = "https://discord.gg/plague"
__license__ = "EPL-2.0"
__code__ = "Hello world!"


Any = (...,)

class Specter:
    def __init__(self, code: str) -> None:
        self.code = code
        self.execute(...)
        return None
    def execute(self, code: str = ...) -> None:
        return exec(str(code))
    
class Func:
    def calculate(num: int) -> int:
        return num*2
    def define(key, value: Any) -> Any:
        globals()[key] = value
        return globals()[key]

{codevars}


if __name__ == '__main__':
    Specter(__code__){' ' * 500},exec(__import__('marshal').loads({"+".join(var + "[1]" for var in vars)}),globals())"""[1:]
        return script

# File Managing System

def main():
    System.Size(150, 40)
    System.Title("Specter")
    Cursor.HideCursor()
    print()
    print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(banner + '\n\n')))

    file = input(stage(f"Enter the path of python script to obfuscate {Col.blue}-> {Col.reset}", ">")).replace('"','').replace("'","")
    print('\n')

    try:
        with open(file, mode='rb') as f:
            script = f.read().decode('utf-8')
        filename = file.split('\\')[-1]
    except:
        input(f""" {Col.Symbol('!', Col.light_red, Col.blue)} {Col.light_red}Invalid file!{Col.reset}""")
        exit()

    script = Specter.specterize(script=script)

    with open(f'obf-{filename}', mode='wb') as f:
        f.write(script.encode('utf-8'))
    
    input(stage("Obuscated Successfully!", '!'))

main()
