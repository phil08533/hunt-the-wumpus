import random

# Game state variables
rooms = {}
player_room = None
wumpus_room = None
alive = True
has_won = False

def generate_map():
    global rooms
    rooms = {i: [(i + 1) % 20, (i + 2) % 20, (i + 3) % 20] for i in range(20)}

def start_game():
    global player_room, wumpus_room, alive, has_won
    generate_map()
    wumpus_room = random.choice(list(rooms.keys()))
    player_room = random.choice([r for r in rooms if r != wumpus_room])
    alive = True
    has_won = False

def move_player(room):
    global player_room, alive
    if room in rooms[player_room]:
        player_room = room
        if player_room == wumpus_room:
            alive = False
    else:
        raise ValueError("Can't move to that room")

def shoot_arrow(room):
    global has_won, alive
    if room == wumpus_room:
        has_won = True
    else:
        alive = False

def get_status():
    return {
        "player_room": player_room,
        "alive": alive,
        "has_won": has_won,
        "adjacent_rooms": rooms[player_room]
    }

# Run game loop
if __name__ == "__main__":
    start_game()
    print("Welcome to Hunt the Wumpus!")

    while alive and not has_won:
        status = get_status()
        print(f"\nYou are in room {status['player_room']}")
        print(f"Adjacent rooms: {status['adjacent_rooms']}")
        action = input("Move (m) or Shoot (s)? ").strip().lower()
        try:
            target = int(input("Which room? "))
            if action == 'm':
                move_player(target)
            elif action == 's':
                shoot_arrow(target)
        except ValueError as ve:
            print("Invalid move or input:", ve)

    if has_won:
        print("You shot the Wumpus! You win!")
    else:
        print("The Wumpus got you. Game over.")