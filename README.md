## How to Run the Game

Make sure you have Docker installed. If not, follow the instructions [here](https://docs.docker.com/get-docker/).

run these commands in bash/terminal one at a time

    git clone https://github.com/phil08533/hunt-the-wumpus.git
    cd hunt-the-wumpus
    docker build -t hunt-the-wumpus .
    docker run -it hunt-the-wumpus




## How to Play Hunt the Wumpus ##
Welcome to Hunt the Wumpus! In this game, you must navigate through a maze of rooms to find and shoot the dangerous Wumpus, while avoiding traps. Here's a quick guide on how to play:

Objective:
    
    Shoot the Wumpus to win the game.

    Avoid moving into the Wumpus's room, or you'll lose.

Game Setup:
   
    There are 20 rooms in the maze, connected to each other.
    
    The Wumpus is placed randomly in one of the rooms.
    
    You are placed in a random room, not the same as the Wumpus.

Gameplay:
    
    Your Current Room: You start in a room and can see which rooms are adjacent to you.
    
    Move: You can move to any adjacent room (shown in the list of adjacent rooms). Be careful! 
    If you move into the Wumpus's room, you lose!
    
    Shoot: You can shoot an arrow into any room. If you hit the Wumpus, you win the game! If you 
    miss, you lose.

Controls:
  
    Move (m): Type m and choose one of the adjacent rooms to move to.
    
    Shoot (s): Type s and choose a room to shoot an arrow at.

Winning the Game:
    
    Shoot the Wumpus: You win if your arrow hits the Wumpus’s room.

Losing the Game:

    Move into the Wumpus’s room: You lose if you step into the Wumpus's room.
    
    Shoot the wrong room: If you miss, the Wumpus is still alive!

