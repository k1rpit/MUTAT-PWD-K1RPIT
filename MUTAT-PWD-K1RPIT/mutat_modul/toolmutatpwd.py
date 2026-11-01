import string

base_endings_list = ['8888','0987654321','1234567890','0000','4321','1234','!','.','.,',',','666','3000','3333','$']
years_list = list(range(1930,2026))
pwd_str = 'Qwerty'





def very_base_mutated_dictionary(*,pwd: str) ->set:
    very_base_mutated_list = [pwd+str(i)+'.' for i in range(11)]
    return set(very_base_mutated_list)



def base_mutated_dictionary(*,pwd: str,endings=base_endings_list) ->set:
    base_mutated_dict = []
    base_mutated_dict.append(pwd)
    base_mutated_dict.append(pwd.upper())
    base_mutated_dict.append(pwd.lower())
    base_mutated_dict.append(pwd.swapcase())
    base_mutated_dict.append(pwd.capitalize())
    base_mutated_dict.append(pwd[::-1])

    for i in endings:
        base_mutated_dict.append(f'{pwd}{i}')
    for i in range(10):
        base_mutated_dict.append(f'{pwd}{i}')

    for i in endings:
        base_mutated_dict.append(f'{pwd.lower()}{i}')
    for i in range(10):
        base_mutated_dict.append(f'{pwd.lower()}{i}')

        
    for i in endings:
        base_mutated_dict.append(f'{pwd.upper()}{i}')
    for i in range(10):
        base_mutated_dict.append(f'{pwd.upper()}{i}')

    for i in endings:
        base_mutated_dict.append(f'{pwd.swapcase()}{i}')
    for i in range(10):
        base_mutated_dict.append(f'{pwd.swapcase()}{i}')

    for i in endings:
        base_mutated_dict.append(f'{pwd.capitalize()}{i}')
    for i in range(10):
        base_mutated_dict.append(f'{pwd.capitalize()}{i}')

    return set(base_mutated_dict)


def moderately_mutated_dictionary(*,pwd: str,year=years_list) -> set:
    symbols = list(string.punctuation)
    moderately_mutated_dict = []
    moderately_mutated_dict.append(pwd*2)
    moderately_mutated_dict.append(pwd*3)
    moderately_mutated_dict.append(pwd)
    moderately_mutated_dict.append(pwd.upper())
    moderately_mutated_dict.append(pwd.lower())
    moderately_mutated_dict.append(pwd.swapcase())
    moderately_mutated_dict.append(pwd.capitalize())
    moderately_mutated_dict.append(pwd[::-1])
    moderately_mutated_dict.append(pwd.lower()[::-1])
    moderately_mutated_dict.append(pwd.upper()[::-1])
    moderately_mutated_dict.append(pwd.capitalize()[::-1])
    moderately_mutated_dict.append(pwd.swapcase()[::-1])
    moderately_mutated_dict.append(pwd[::2])
    moderately_mutated_dict.append(pwd.lower()[::2])
    moderately_mutated_dict.append(pwd.upper()[::2])
    moderately_mutated_dict.append(pwd.capitalize()[::2])
    moderately_mutated_dict.append(pwd.swapcase()[::2])

    for i in year:
        moderately_mutated_dict.append(f'{pwd}{i}')
        moderately_mutated_dict.append(f'{pwd * 2}{i}')
    for i in range(10):
        moderately_mutated_dict.append(f'{pwd}{i}')
        moderately_mutated_dict.append(f'{pwd * 2}{i}')

    for i in year:
        moderately_mutated_dict.append(f'{pwd.lower()}{i}')
        moderately_mutated_dict.append(f'{pwd.lower() * 2}{i}')
    for i in range(10):
        moderately_mutated_dict.append(f'{pwd.lower()}{i}')
        moderately_mutated_dict.append(f'{pwd.lower() * 2}{i}')

    for i in year:
        moderately_mutated_dict.append(f'{pwd.upper()}{i}')
        moderately_mutated_dict.append(f'{pwd.upper() * 2}{i}')
    for i in range(10):
        moderately_mutated_dict.append(f'{pwd.upper()}{i}')
        moderately_mutated_dict.append(f'{pwd.upper() * 2}{i}')

    for i in year:
        moderately_mutated_dict.append(f'{pwd.swapcase()}{i}')
        moderately_mutated_dict.append(f'{pwd.swapcase() * 2}{i}')
    for i in range(10):
        moderately_mutated_dict.append(f'{pwd.swapcase()}{i}')
        moderately_mutated_dict.append(f'{pwd.swapcase() * 2}{i}')

    for i in year:
        moderately_mutated_dict.append(f'{pwd.capitalize()}{i}')
        moderately_mutated_dict.append(f'{pwd.capitalize() * 2}{i}')
    for i in range(10):
        moderately_mutated_dict.append(f'{pwd.capitalize()}{i}')
        moderately_mutated_dict.append(f'{pwd.capitalize() * 2}{i}')

    for i in symbols:
        moderately_mutated_dict.append(f'{pwd}{i}')
        moderately_mutated_dict.append(f'{pwd * 2}{i}')

    for i in symbols:
        moderately_mutated_dict.append(f'{pwd.lower()}{i}')
        moderately_mutated_dict.append(f'{pwd.lower() * 2}{i}')
        

    for i in symbols:
        moderately_mutated_dict.append(f'{pwd.upper()}{i}')
        moderately_mutated_dict.append(f'{pwd.upper() * 2}{i}')
    
    for i in symbols:
        moderately_mutated_dict.append(f'{pwd.swapcase()}{i}')
        moderately_mutated_dict.append(f'{pwd.swapcase() * 2}{i}')

    for i in symbols:
        moderately_mutated_dict.append(f'{pwd.capitalize()}{i}')
        moderately_mutated_dict.append(f'{pwd.capitalize() * 2}{i}')


    


    

    return set(moderately_mutated_dict)



