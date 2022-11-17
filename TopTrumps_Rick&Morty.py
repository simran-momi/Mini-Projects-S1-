import os, time, random

trumps = {}
trumps["Rick"] = {'Morality': 26, 'Intelligence': 86, 'Violence': 62, 'Shwifty Factor': 100}
trumps['Morty'] = {'Morality': 63, 'Intelligence': 39,  'Violence': 44, 'Shwifty Factor': 70}
trumps['Beth'] = {'Morality': 44, 'Intelligence': 72, 'Violence': 47, 'Shwifty Factor': 48}
trumps['Jerry'] = {'Morality': 86, 'Intelligence': 60, 'Violence': 21, 'Shwifty Factor': 15}
trumps['Summer'] = {'Morality': 30, 'Intelligence': 70,  'Violence': 85, 'Shwifty Factor': 80}
trumps['Mr Meeseeks'] = {'Morality': 70, 'Intelligence': 60, 'Violence': 30, 'Shwifty Factor': 60}
trumps['Mr Poopybutthole'] = {'Morality': 63, 'Intelligence': 39, 'Violence': 30, 'Shwifty Factor': 50}
trumps['Dr Xenon Bloom'] = {'Morality': 70, 'Intelligence': 80, 'Violence': 15, 'Shwifty Factor': 48}
trumps['Jessica'] = {'Morality': 52, 'Intelligence': 41, 'Violence': 30, 'Shwifty Factor': 5}
trumps['Dr Wong'] = {'Morality': 78, 'Intelligence': 72, 'Violence': 28, 'Shwifty Factor': 50}

while True:
    print('RICK & MORTY TOP TRUMPS')
    print('***********************')
    print('character options:')
    print('***********************')
    for key in trumps:
        print(key)
    user = input('Pick your character\n> ')
    comp = random.choice(list(trumps.keys()))
    print('Computer has picked', comp)

    print('Choose your stat: Morality, Intelligence, Violence & Shwifty Factor')

    answer = input('> ')

    print(f'{user}: {trumps[user][answer]}')
    print(f'{comp}: {trumps[comp][answer]}')

    if trumps[user][answer] > trumps[comp][answer]:
        print(user, 'wins, CONGRATS!')
    elif trumps[user][answer]< trumps[comp][answer]:
        print(comp, 'wins, BETTER LUCK NEXT ROUND!')
    else:
        print('ITS A DRAW!')

        time.sleep(5)
        os.system('clear')