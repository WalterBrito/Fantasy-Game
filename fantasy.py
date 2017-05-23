import random
import textwrap
import sys

def show_theme_message(width):
    msg = (
        "The war between humans and their arch enemies, the Orcs, was in the offing. A"
        "huge army of Orcs was heading toward the human establishments. They were"
        "virtually destroying everything in their way. The great kings of the human race"
        "joined hands to defeat their worst enemy for the great battle of their time. Men were"
        "summoned to join the rest of the army. Sir Foo, one of the brave knights guarding"
        "the southern plains, began a long journey toward the east, through an unknown"
        "dense forest. For two days and two nights, he moved cautiously through the thick"
        "woods. On his way, he spotted a small isolated settlement. Tired and hoping to"
        "replenish his food stock, he decided to take a detour. As he approached the village, he"
        "saw five huts. There was no one to be seen around. Hesitantly, he decided to enter a hut..."
    )

    print(textwrap.fill(msg, width=width))

def show_game_misison():
    print_bold("Mission:")
    print("\tChoose a hut where Sir Foo can rest...")
    print("TIP:")
    print("Be careful as there are enemies lurking around!")
    print_dotted_line()

def reveal_occuapnts(idx, huts):
    msg = ""
    print("Revealing the occupants...")
    for i in range(len(huts)):
        occupant_info = "<%d:%s>%(i+1, huts[i])"
        if i + 1 == idx:
            occupant_info = "\033[1m" + occupant_info + "\033[0m"
        msg += occupant_info + " "
    print("\t" + msg)
    print_dotted_line()

def occupy_huts():
    """Randomly populate the `huts` list with occupants"""
    huts = []
    occupants = ['enemy', 'friend', 'unoccupied']
    while len(huts) < 5:
        computer_choice = random.choice(occupants)
        huts.append(computer_choice)
    return huts

def process_user_choice():
    """Accepts the hut number from the user"""
    msg = "\033[1m" + "Choose a hut number to enter (1-5): " + "\033[0m"
    user_choice = input("\n" + msg)
    idx = int(user_choice)
    return idx

def show_health(health_meter, bold=False):
    """Show the remaining hit points of the player and the enemy"""
    msg = "Health: Sir Foo: %d, Enemy: %d" % (health_meter['player'], health_meter['enemy'])

    if bold:
        print_bold(msg)
    else:
        print(msg)

def reset_health_meter(health_meter):
    """Reset the values of health_meter dict to the original ones"""
    health_meter['player'] = 40
    health_meter['enemy'] = 30

def print_bold(msg, end='\n'):
    """Print a string in 'bold' font"""
    print('-' * width)

def attack(health_meter):
    """The main logic to determine injured unit and amount of injury"""
    hit_list = 4 * ['player'] + 6 ['enemy']
    injured_unit = random.choice(hit_list)
    hit_points = health_meter[injured_unit]
    injury = random.randint(10, 15)
    health_meter[injured_unit] = max(hit_points - injury, 0)
    print("ATTACK!", end='')
    show_health(health_meter)








if __name__=='__main__':
    keep_playing = 'y'
    width = 72
    dotted_line = '-' * width
    print(dotted_line)
    print("\033[1m" + "Attack of the Orcs v0.0.1:" + "\033[0m")




    while keep_playing == 'y':
        # Randomly append 'enemy' or 'friend' or None the huts list


        # Prompt user to select a hut


        # Print the occupant info

        print(dotted_line)
        print("\033[1m" + "Entering hut %d..." % idx + "\033[0m", end=' ')

        # Determine and announce the winner
        if huts[idx-1] == 'enemy':
            print("\033[1m" + "YOU LOSE :( Better luck next time! " + "\033[0m")
        else:
            print("\033[1m" + "Congratulations! YOU WIN!!!" + "\033[0")
        print(dotted_line)
        keep_playing = input("Play again? Yes(y)/No(n): ")