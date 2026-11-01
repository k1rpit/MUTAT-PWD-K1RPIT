from mutat_modul.toolmutatpwd import very_base_mutated_dictionary,base_mutated_dictionary,moderately_mutated_dictionary
from sys import argv,exit

sys_argv = argv[1:]



def main(*,arg: list):
    try:
        if arg[0] == '-vb':
            pws_dict=list(very_base_mutated_dictionary(pwd=arg[1]))
        elif arg[0] == '-b':
            pws_dict=list(base_mutated_dictionary(pwd=arg[1]))
        elif arg[0] == '-m':
            pws_dict=list( moderately_mutated_dictionary(pwd=arg[1]))
        elif arg[0] == '--help':
            print('''
            -vb\tA very simple mutation that adds digits (in the range 0–10) and '.';
            -b\ta simple mutation out of 101 variants
            -m\tdeep-level mutation variants out of ~1000 possibilities

            syntax:python3 main.py <argv> <word>
            ''')
        else:
            print('''
            syntax:python3 main.py <argv> <word>
            for help, enter "--help"
            ''')
    except IndexError:

            print('''
            syntax:python3 main.py <argv> <word>
            for help, enter "--help"
            ''')
            exit('no argv!')
    try:
        with open('dict-pwd.txt','w') as f:
            for i in pws_dict:
                f.write(f'{i}\n')
    except UnboundLocalError:
        exit()
        
        
if __name__ == "__main__":
    main(arg=sys_argv)