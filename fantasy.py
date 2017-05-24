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

def reveal_occupants(idx, huts):
    """Print the occupants of the hut"""
    msg = ""
    print("Revealing the occupants...")
    for i in range(len(huts)):
        occupant_info = "<%d:%s>" % (i+1, huts[i])
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
    print("\033[1m" + msg + "\033[0m", end=end)

def print_dotted_line(width=72):
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

def play_game(health_meter):
    huts = occupy_huts()
    idx = process_user_choice()
    reveal_occupants(idx, huts)

    if huts[idx - 1] != 'enemy':
        print_bold("Congratulations! YOU WIN!!!")
    else:
        print_bold('ENEMY SIGHTED!', end='')
        show_health(health_meter, bold=True)
        continue_attack = True

        # Loop that actually runs the combat if user wants to attack
        while continue_attack:
            continue_attack = input(".......continue attack? (y/n): ")
            if continue_attack == 'n':
                print_bold("RUNNING AWAY  with following health status...")
                show_health(health_meter, bold=True)
                print_bold("GAME OVER!")
                break

            attack(health_meter)

            # Check if either one of the opponents is defeated
            if health_meter['enemy'] <= 0:
                print_bold("GOOD JOB! Enemy defeated! YOU WIN!!!")
                break

            if health_meter['player'] <= 0:
                print_bold("YOU LOSE! :( Better luck next time")
                break
def run_application():
    """Top level control function for running the application."""
    keep_playing = 'y'
    health_meter = {}
    reset_health_meter(health_meter)
    show_game_misison()

    while keep_playing == 'y':
        reset_health_meter(health_meter)
        play_game(health_meter)
        keep_playing = input("\nPlay again? Yes(y)/No(n): ")

if __name__ == '__main__':
    run_application()