# Reversi_AI
AI that plays the game Reversi or Othello (can play against Human Players or Other AI) <br/>

To run the server and game GUI, type in the command line: java Reversi [time] <br/>
--->[time] represents and integer which is the number of total minutes you want each player to have to play the game <br/>
--->For a game in which each player has 10 minutes, type jave Reversi 10 <br/>

To run the AI against a human player, type in a separate command line: python python_reversi_client.py localhost [playerNum] [time] <br/>
--->[playerNum] is an integer either 1 or 2 that decides if the AI is 1st or 2nd player <br/>
--->[time] again in an integer which is the total minutes you want each player to play the game -> This number must match the one typed into the server! <br/>
--->localhost can be replaced with a server IP address if the server is running on a different machine <br/>
--->For a 10 minute game in which the computer is player 1: python python_reversi_client.py localhost 1 10

To run the AI against a computer player or another AI, type in a separate command line the command for running your AI. <br/>
Alternatively, you can run my AI against a random move AI by typing in a separate command line: java RandomGuy [playerNum]

**The framework and GUI code for this project was written by Professor Jacob Crandall <br/>
**Elizabeth Van Patten wrote the file that contains the algorithm that runs the AI
