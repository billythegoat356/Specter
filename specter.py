from marshal import dumps
from binascii import hexlify
import os
from random import choice, randint, shuffle
import string

from pystyle import *


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



class Specter:
    
    def RandomName():
        # add more to the msgs if you want.
        msgs = ["Hello_world", "Skids_are_confused", "o", "imagine", "skull", "Omega", "Lol", "Skids_mad", "Fo_Sho", "nice_Work", "dont_know_how_to_deobf_L"]
        name = choice(msgs)
        add_underscore = choice([True, False])  # add __ with 50% chance
        
        if add_underscore:
            name = '__' + name + '__'
        
        random_letters = ''.join(choice(string.ascii_letters) for i in range(randint(1, 5)))  # add random letters
        name += random_letters
        
        return name

    def RandomMessage():
        msgs = ["Hello world!", "Are you having fun trying to deobf", "Skid protection 4 the win", "Cant read the code and make a deobf? That sucks lol", "Imagine thinking __code__ is useful.", "Skids are confused!!!", "imagine", "Omega Ώ", "Lol", "Skids mad!!!", "Fo Sho"]

        t = choice(msgs)

        return t

    RandName = RandomName()
    Msg = RandomMessage()

    vars = []

    def specterize(script: str) -> str:
        print(stage("Starting specterization!"))
        # print(stage("Preparing anti skid layer...")) just to be sure
        script = Specter.anti_skid(script=script)
        print(stage("Adding layer 1!"))
        script = Specter.layer_1(script=script)
        print(stage("Adding layer 2!"))
        script = Specter.layer_2(script=script)
        print(stage("Adding layer 3!"))
        script = Specter.layer_3(script=script)
        return script

    def hex(text: str) -> bytes:
        return "b'" + "".join(fr"\x{hexlify(t.encode('utf-8')).decode()}" for t in text) + "'"

    def encrypt(text: str, key: int) -> str:
        return "\x00".join(str(ord(x)+key) for x in text)

    def randvar() -> str:
        var = randint(1000, 9999)
        while var in Specter.vars:
            var = randint(1000, 9999)
        Specter.vars.append(var)
        return f"__{var}__"
    
    def get_key_by_value(vars, key) -> str:
        return list(vars.keys())[list(vars.values()).index(key)]

    def anti_skid(script: str) -> str:
        return fr"""
# GG! You just deobfuscated Specter

# https://github.com/billythegoat356/Specter

# by billythegoat356

# join discord.gg/plague for more Python tools!


try:
    if (
        __author__ != "billythegoat356" or
        __github__ != "https://github.com/billythegoat356/Specter" or
        __discord__ != "https://discord.gg/plague" or
        __license__ != "EPL-2.0" or
        __code__ != '{Specter.Msg}' or
        "{Specter.RandName}" not in globals() or
        "Func" not in globals()
    ):
        int('skid')
except Exception as e:
    input("You just executed a file obfuscated with Specter!\n\nAuthor: billythegoat356\nGitHub: https://github.com/billythegoat356/Specter\nDiscord: https://discord.gg/plague")
    print(e)
    __import__('sys').exit()    


"""[1:] + script

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
        print(stage("Creating random vars..."))
        lambdas = [fr"{l1}=lambda {l2}:''.join(chr(int({l3})-int({lkey}))for {l3} in {l2}.decode().split('\x00'))",
                   f"(lambda {l3}:{glob}(''.join({l1}({l2}={l2})for {l2} in {l3}),{Specter.get_key_by_value(vars, 'globals')}()))([{','.join(all_correct)}])",]
        script = "from builtins import *\n" + script + '\n'.join(lambdas)
        return script

    def layer_2(script: str) -> str:
        print(stage("Compiling and dumping code with marshal..."))
        return dumps(compile(script, 'Specter', 'exec'))

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
        print(stage("Camouflation of the obfuscated code..."))
        script = fr"""
# this code has been obfuscated with Specter

# https://github.com/billythegoat356/Specter

# by billythegoat356

# join discord.gg/plague for more Python tools!


__author__ = "billythegoat356"
__github__ = "https://github.com/billythegoat356/Specter"
__discord__ = "https://discord.gg/plague"
__license__ = "EPL-2.0"
__code__ = '{Specter.Msg}'


Any = (...,)

class {Specter.RandName}:
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
    {Specter.RandName}(__code__){' ' * 1000},exec(__import__('marshal').loads({"+".join(var + "[1]" for var in vars)}),globals())"""[1:]
        return script


def main():
    System.Size(150, 40)
    System.Title("Specter")
    Cursor.HideCursor()
    print()
    print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(banner + '\n\n')))

    file = input(stage(f"Drag the file you want to obfuscate {Col.blue}-> {Col.reset}", "?")).replace('"','').replace("'","")
    print('\n')
    
    path = os.path.dirname(file) # gets the path of the file created. This is so it isnt created in the logged into profiles folder: e.g C:/Users/Name_Here/obf-name.py
    
    # print(path)  # ptints path, debugging

    try:

        with open(file, mode='rb') as f:

            script = f.read().decode('utf-8')

        filename = file.split('\\')[-1]

    except:
        input(f""" {Col.Symbol('!', Col.light_red, Col.blue)} {Col.light_red}Invalid file!{Col.reset}""")
        exit()

    script = Specter.specterize(script=script)
    
    try:
        with open(os.path.join(path, f'obf-{filename}'), mode='wb') as f:
            f.write(script.encode('utf-8'))


        print(f'''{Col.Symbol('!', Col.light_red, Col.blue)} {Col.light_red}Created at: {os.path.join(path, f'obf-{filename}')}{Col.reset}''') # prints the files path 

        print('\n')
        input(stage("Done!", '!'))
    except Exception as e:
        input(f""" {Col.Symbol('!', Col.light_red, Col.blue)} {Col.light_red}Error Writing to obf-{filename}!{Col.reset}""")
        print(f"{Col.Symbol('!', Col.light_red, Col.blue)}{Col.light_red}{e}{Col.reset}")

main()
