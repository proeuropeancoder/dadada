import random

class MatchSimulator:
    def __init__(self):
        self.players = {
            "Goalkeepers": ["Stole Dimitrievski", "Joan Garcia"],
            "Center-Backs": ["Balerdi", "Huijsen", "Branthwaite", "Krejci", "Raul Asencio"],
            "Wing-Backs": ["Hector Fort", "Livramento"],
            "Midfielders": ["Reijnders", "Merino", "Enzo Fernández", "Dani Olmo", "Mikel Merino"],
            "Wingers": ["Kvaratskhelia", "Palmer", "Garnacho", "Alexis Saelemaekers", "Ferran Torres"],
            "Strikers": ["Gyökeres", "Miovski", "Ferran Torres", "Merino", "Palmer"]
        }

        self.starting_xi = {
            "GK": "Stole Dimitrievski",
            "CB": ["Balerdi", "Huijsen", "Branthwaite"],
            "LWB": "Hector Fort",
            "RWB": "Livramento",
            "CM": ["Reijnders", "Merino"],
            "LW": "Kvaratskhelia",
            "ST": "Gyökeres",
            "RW": "Palmer"
        }

        self.bench = ["Krejci", "Raul Asencio", "Enzo Fernández", "Dani Olmo", 
                      "Garnacho", "Saelemaekers", "Miovski", "Ferran Torres", "Mikel Merino"]

        self.score = [0, 0]
        self.commentary = []

    def run_match(self):
        self.score = [0, 0]
        self.commentary = []

        for minute in range(1, 91):
            event_chance = random.randint(1, 100)

            if event_chance > 97:
                scorer = random.choice([self.starting_xi['ST'], self.starting_xi['LW'], self.starting_xi['RW']])
                self.score[0] += 1
                self.commentary.append(f"{minute}': GOAL! {scorer} scores for your team!")
            elif event_chance < 3:
                self.score[1] += 1
                self.commentary.append(f"{minute}': OPPONENT GOAL!")

            elif 40 <= event_chance < 50:
                pool = self.bench + self.starting_xi['CB'] + [self.starting_xi['LWB'], self.starting_xi['RWB']] + self.starting_xi['CM'] + [self.starting_xi['LW'], self.starting_xi['RW'], self.starting_xi['ST']]
                player = random.choice(pool)
                self.commentary.append(f"{minute}': {player} makes a key play!")

            if minute in [45, 60, 75] and self.bench:
                sub_choice = random.choice(self.bench)
                replaced = None
                for key, value in self.starting_xi.items():
                    if isinstance(value, list):
                        for i, p in enumerate(value):
                            value[i] = sub_choice
                            replaced = p
                            break
                        if replaced:
                            break
                    elif key in ["GK", "LWB", "RWB", "LW", "RW", "ST"]:
                        replaced = self.starting_xi[key]
                        self.starting_xi[key] = sub_choice
                        break
                self.bench.remove(sub_choice)
                if replaced:
                    self.bench.append(replaced)
                    self.commentary.append(f"{minute}': SUBSTITUTION! {sub_choice} comes on for {replaced}.")

        self.commentary.append(f"🏁 FULL TIME! FINAL SCORE: {self.score[0]} - {self.score[1]}")
        return self.commentary, self.score
