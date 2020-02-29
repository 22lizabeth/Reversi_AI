# Reversi_AI
AI that plays the game Reversi or Othello (can play against Human Players or Other AI) <br/>

Note: All Java classes are already compiled. <br/>

To run the server and game GUI, make sure you are in the ReversiServer directory and type in the command line: <br/>
<strong>java Reversi [time] </strong><br/>
--->[time] represents and integer which is the number of total minutes you want each player to have to play the game <br/>
--->For a game in which each player has 10 minutes, type java Reversi 10 <br/>

To run the AI, open a second command line and go to the ReversiAI directory then type the following: <br/>
  <strong>python python_reversi_client.py localhost [playerNum] [time] </strong> <br/>
--->[playerNum] is an integer either 1 or 2 that decides if the AI is 1st or 2nd player <br/>
--->[time] again in an integer which is the total minutes you want each player to play the game -> This number must match the one typed into the server! <br/>
--->localhost can be replaced with a server IP address if the server is running on a different machine <br/>
--->For a 10 minute game in which the computer is player 1: python python_reversi_client.py localhost 1 10

To run the AI against a human player, open a third command line and go to the ReversiHuman directory then type the following: <br/>
<strong>java Human localhost [playerNum]</strong> <br/>
--->[playerNum] is an integer either 1 or 2 and MUST be different than the playerNum assigned to the AI <br/>
--->localhost can be replaced with a server IP address <br/>

To run the AI against a computer player or another AI, type in a third line the command for running your AI. <br/>

To run the AI against a random move AI, open a third command line and go to the ReversiRandom directory then type the following: <br/>
<strong>java RandomGuy localhost [playerNum]</strong><br/>
--->[playerNum] is an integer either 1 or 2 and MUST be different than the playerNum assigned to the AI<br/>
--->localhost can be replaced with a server IP address <br/>

<hr>
<strong>**The framework and GUI code for this project was written by Professor Jacob Crandall (this includes all code in ReversiServer, ReversiRandom, and ReversiHuman folders) </strong><br/><br/>
<strong>**Elizabeth Van Patten wrote the entire file that contains the algorithm that runs the AI (found in ReversiAI/reversi_bot.py </strong>
