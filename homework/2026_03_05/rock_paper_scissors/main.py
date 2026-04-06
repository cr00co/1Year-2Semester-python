class RockPaperScissors:
    def __init__(self):
        while True:
            try:
                number_of_players = int(input("Enter number of players: "))
                if 2 <= number_of_players <= 6:
                    break
                print("\nNumber of players must be between 2 and 6!\n")
            except ValueError:
                print("\nInvalid number of players!\n")

        self.plrs = {}

        for i in range(number_of_players):
            name = input(f"Enter {i + 1} player's name: ")
            self.plrs[name] = {"points": 0, "move": None}
        
        self.wins_against = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
    
    def play_round(self):
        moves = ['rock', 'paper', 'scissors']

        for name in self.plrs:
            while True:
                move = input(f"{name}, enter your move(rock/paper/scissors): ").lower()
                if move in moves:
                    self.plrs[name]["move"] = move
                    break
                print("\nInvalid move, try again.\n")

        moves_played = {data["move"] for data in self.plrs.values()}
        if moves_played == {'rock', 'paper', 'scissors'}:
            print("\nAll three moves played - it's a draw, so no one gets a point!")
            return

        round_winners = set()
        names = list(self.plrs.keys())

        for i in range(len(names)):
            for j in range(i+1, len(names)):
                a, b = names[i], names[j]
                move_a = self.plrs[a]["move"]
                move_b = self.plrs[b]["move"]

                if self.wins_against[move_a] == move_b:
                    round_winners.add(a)
                elif self.wins_against[move_b] == move_a:
                    round_winners.add(b)

        if round_winners:
            for winner in round_winners:
                self.plrs[winner]["points"] += 1
            print(f"\nRound winners: {', '.join(round_winners)}")
        else:
            print(f"\nEveryone played the same move — it's a draw, no one gets a point!")

    def is_game_over(self):
        return any(data["points"] >= 3 for data in self.plrs.values())

    def get_result(self):
        final_scores = "\n".join(f"{name}: {data["points"]}" for name, data in self.plrs.items())
        winners = [name for name, data in self.plrs.items() if data["points"] == 3]
        
        if len(winners) > 1:
            winners_str = ", ".join(winners)
            return (f"The game has ended.\n\nFinal scores:\n{final_scores}\n\n"
                    f"It's a tie between {winners_str}!")
        else:
            return (f"The game has ended.\n\nFinal score:\n{final_scores}\n\n"
                    f"Congratulations, {winners[0]}!")
        
    def print_score(self):
        current_scores = " | ".join(f"{name} [{data["points"]}]" for name, data in self.plrs.items())
        print(f"\nCurrent scores: {current_scores}\n")

    def run(self):
        while not self.is_game_over():
            self.play_round()
            self.print_score()

        print(self.get_result())


if __name__ == "__main__":
    RockPaperScissors().run()



