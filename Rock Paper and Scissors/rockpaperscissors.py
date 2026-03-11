import random

class RockPaperScissors:

    MOVES = ["rock", "paper", "scissors"]

    def __init__(self):
        self.leaderboard = {}
        self.stats = {}
    
    def winner(self, p1, p2):

        if p1 == p2:
            return 0
        
        if (p1 == "rock" and p2 == "scissors") or \
        (p1 == "scissors" and p2 == "paper") or \
        (p1 == "paper" and p2 == "rock"):
            return 1
        
        else:
            return 2


    def player_move(self, player):

        move = input(f"{player} enter (rock/paper/scissors): ").lower()

        while move not in self.MOVES:
            move = input("Invalid! Enter rock/paper/scissors: ").lower()

        return move

    def computer_mode(self, rounds):

        your_score = 0
        computer_score = 0

        for r in range(1, rounds+1):

            print("\nRound - ",r)

            your_move = self.player_move("You")
            computer_move = random.choice(self.MOVES)

            print("Computer chose:", computer_move)

            result = self.winner(your_move, computer_move)

            if result == 1:
                your_score += 1
                print("You win")
            elif result == 2:
                computer_score += 1
                print("Computer wins")
            else:
                print("Tie")

        print("\nFinal Score:", your_score, "-", computer_score)

        self.update_score("You", your_score)


    def two_player(self, p1, p2, rounds):

        player1_score= 0
        player2_score = 0

        for r in range(1, rounds+1):

            print("\nRound - ",r)

            m1 = self.player_move(p1)
            m2 = self.player_move(p2)

            result = self.winner(m1, m2)

            if result == 1:
                player1_score += 1
                print(p1, "wins")
                self.update_stats(p1, win=True)
                self.update_stats(p2, loss=True)

            elif result == 2:
                player2_score += 1
                print(p2, "wins")
                self.update_stats(p2, win=True)
                self.update_stats(p1, loss=True)
                
            else:
                print("Tie")
                self.update_stats(p1)
                self.update_stats(p2)

        print("\nFinal Score:", p1, player1_score, "|", p2, player2_score)

        self.update_score(p1, player1_score)
        self.update_score(p2, player2_score)


    def elimination(self, players):

        print("\n--- Elimination Tournament ---")

        while len(players) > 1:

            random.shuffle(players)
            next_round = []

            if len(players) % 2 == 1:
                bye = players.pop()
                print(bye, "Player gets a bye to next round")
                next_round.append(bye)

            for i in range(0, len(players), 2):

                p1 = players[i]
                p2 = players[i+1]

                print("\nMatch:", p1, "vs", p2)

                player1_score = 0
                player2_score = 0

                while player1_score < 2 and player2_score < 2:

                    m1 = self.player_move(p1)
                    m2 = self.player_move(p2)

                    result = self.winner(m1, m2)

                    if result == 0:
                        print("Tie replay")
                    elif result == 1:
                        player1_score += 1
                    else:
                        player2_score += 1

                if player1_score > player2_score:
                    print(p1, "wins match")
                    next_round.append(p1)
                else:
                    print(p2, "wins match")
                    next_round.append(p2)

            players = next_round

        print("\nChampion:", players[0])

        self.update_score(players[0], 5)


    def player_stats(self):

        print("\n------ Player Statistics ------")

        if len(self.stats) == 0:
            print("No data available")
            return

        for player, data in self.stats.items():

            matches = data["matches"]
            wins = data["wins"]
            losses = data["losses"]

            if matches == 0:
                win_rate = 0
            else:
                win_rate = (wins / matches) * 100

            print("\nPlayer:", player)
            print("Matches :", matches)
            print("Wins    :", wins)
            print("Losses  :", losses)
            print("Win %   :", round(win_rate,2))
        
    def update_stats(self, name, win=False, loss=False):

        if name not in self.stats:
            self.stats[name] = {"matches":0, "wins":0, "losses":0}

        self.stats[name]["matches"] += 1

        if win:
            self.stats[name]["wins"] += 1

        if loss:
            self.stats[name]["losses"] += 1 

    def update_score(self, name, score):

        if name in self.leaderboard:
            self.leaderboard[name] += score
        else:
            self.leaderboard[name] = score

    def players_leaderboard(self):

        print("\n----------Leaderboard-----------")
        if len(self.leaderboard) == 0:
            print("No data available")
            return

        ranking = sorted(self.leaderboard.items(),key=lambda x: x[1], reverse=True)

        pos = 1
        for name, score in ranking:
            print(pos, ".", name, "->", score, "pts")
            pos += 1

    def reset_leaderboard(self):
        self.leaderboard.clear()
        print("\nLeaderboard has been reset successfully.")

game = RockPaperScissors()

while True:
    print("\n*******Battle Of Hands (Rock Paper and Scissors Arena******")
    print("1. Computer Mode")
    print("2. Two Player Mode")
    print("3. Elimination Tournament")
    print("4. Leaderboard")
    print("5. Player Statistics")
    print("6. Reset Leaderboard")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        r = int(input("Rounds: "))
        game.computer_mode(r)

    elif choice == "2":
        p1 = input("Player1: ")
        p2 = input("Player2: ")
        r = int(input("Rounds: "))

        game.two_player(p1,p2,r)

    elif choice == "3":
        n = int(input("Number of players: "))

        players = []

        for i in range(n):
            name = input(f"Player {i+1}: ")
            players.append(name)

        game.elimination(players)
            

    elif choice == "4":
        game.players_leaderboard()

    elif choice == "5":
        game.player_stats()

    elif choice == "6":
        game.reset_leaderboard()

    elif choice == "7":
        print("Exiting Game")
        break

    else:
        print("Invalid choice")

# *******Battle Of Hands (Rock Paper and Scissors Arena******
# 1. Computer Mode
# 2. Two Player Mode
# 3. Elimination Tournament
# 4. Leaderboard
# 5. Player Statistics
# 6. Reset Leaderboard
# 7. Exit
# Enter choice: 1
# Rounds: 3

# Round -  1
# You enter (rock/paper/scissors): rock
# Computer chose: scissors
# You win

# Round -  2
# You enter (rock/paper/scissors): paper
# Computer chose: paper
# Tie

# Round -  3
# You enter (rock/paper/scissors): paper
# Computer chose: rock
# You win

# Final Score: 2 - 0

# *******Battle Of Hands (Rock Paper and Scissors Arena******
# 1. Computer Mode
# 2. Two Player Mode
# 3. Elimination Tournament
# 4. Leaderboard
# 5. Player Statistics
# 6. Reset Leaderboard
# 7. Exit
# Enter choice: 2
# Player1: kishore 
# Player2: kumar
# Rounds: 3

# Round -  1
# kishore enter (rock/paper/scissors): rock
# kumar enter (rock/paper/scissors): paper
# kumar wins

# Round -  2
# kishore enter (rock/paper/scissors): rock
# kumar enter (rock/paper/scissors): scissors
# kishore wins

# Round -  3
# kishore enter (rock/paper/scissors): rock 
# kumar enter (rock/paper/scissors): paper
# kumar wins

# Final Score: kishore 1 | kumar 2

# *******Battle Of Hands (Rock Paper and Scissors Arena******
# 1. Computer Mode
# 2. Two Player Mode
# 3. Elimination Tournament
# 4. Leaderboard
# 5. Player Statistics
# 6. Reset Leaderboard
# 7. Exit
# Enter choice: 4

# ----------Leaderboard-----------
# 1 . You -> 2 pts
# 2 . kumar -> 2 pts
# 3 . kishore -> 1 pts

# *******Battle Of Hands (Rock Paper and Scissors Arena******
# 1. Computer Mode
# 2. Two Player Mode
# 3. Elimination Tournament
# 4. Leaderboard
# 5. Player Statistics
# 6. Reset Leaderboard
# 7. Exit
# Enter choice: 6

# Leaderboard has been reset successfully.

# *******Battle Of Hands (Rock Paper and Scissors Arena******
# 1. Computer Mode
# 2. Two Player Mode
# 3. Elimination Tournament
# 4. Leaderboard
# 5. Player Statistics
# 6. Reset Leaderboard
# 7. Exit
# Enter choice: 5

# ------ Player Statistics ------

# Player: kumar
# Matches : 3
# Wins    : 2
# Losses  : 1
# Win %   : 66.67

# Player: kishore
# Matches : 3
# Wins    : 1
# Losses  : 2
# Win %   : 33.33

# *******Battle Of Hands (Rock Paper and Scissors Arena******
# 1. Computer Mode
# 2. Two Player Mode
# 3. Elimination Tournament
# 4. Leaderboard
# 5. Player Statistics
# 6. Reset Leaderboard
# 7. Exit
# Enter choice: 3
# Number of players: 4      
# Player 1: kishore
# Player 2: manoj
# Player 3: karthick
# Player 4: venkat

# --- Elimination Tournament ---

# Match: manoj vs venkat
# manoj enter (rock/paper/scissors): rock
# venkat enter (rock/paper/scissors): paper
# manoj enter (rock/paper/scissors): paper
# venkat enter (rock/paper/scissors): rock
# manoj enter (rock/paper/scissors): rock
# venkat enter (rock/paper/scissors): rock
# Tie replay
# manoj enter (rock/paper/scissors): paper
# venkat enter (rock/paper/scissors): rock
# manoj wins match

# Match: kishore vs karthick
# kishore enter (rock/paper/scissors): rock
# karthick enter (rock/paper/scissors): paper
# kishore enter (rock/paper/scissors): paper
# karthick enter (rock/paper/scissors): rock
# kishore enter (rock/paper/scissors): rock
# karthick enter (rock/paper/scissors): paper
# karthick wins match

# Match: manoj vs karthick
# manoj enter (rock/paper/scissors): paper
# karthick enter (rock/paper/scissors): rock
# manoj enter (rock/paper/scissors): rock
# karthick enter (rock/paper/scissors): scissors
# manoj wins match

# Champion: manoj

# *******Battle Of Hands (Rock Paper and Scissors Arena******
# 1. Computer Mode
# 2. Two Player Mode
# 3. Elimination Tournament
# 4. Leaderboard
# 5. Player Statistics
# 6. Reset Leaderboard
# 7. Exit
# Enter choice: 5

# ------ Player Statistics ------

# Player: kumar
# Matches : 3
# Wins    : 2
# Losses  : 1
# Win %   : 66.67

# Player: kishore
# Matches : 3
# Wins    : 1
# Losses  : 2
# Win %   : 33.33

# *******Battle Of Hands (Rock Paper and Scissors Arena******
# 1. Computer Mode
# 2. Two Player Mode
# 3. Elimination Tournament
# 4. Leaderboard
# 5. Player Statistics
# 6. Reset Leaderboard
# 7. Exit
# Enter choice: 4

# ----------Leaderboard-----------
# 1 . manoj -> 5 pts

# *******Battle Of Hands (Rock Paper and Scissors Arena******
# 1. Computer Mode
# 2. Two Player Mode
# 3. Elimination Tournament
# 4. Leaderboard
# 5. Player Statistics
# 6. Reset Leaderboard
# 7. Exit
# Enter choice: 7
# Exiting Game