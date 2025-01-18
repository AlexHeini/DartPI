# Hier wird die Logik fÃ¼r Spielmodi wie 301 oder 501 hinzugefÃ¼gt.
class Game:
    def __init__(self, players, mode=301):
        """
        Initialisiert ein neues Spiel.
        :param players: Liste der Spielernamen.
        :param mode: Punktestand, mit dem gespielt wird (z. B. 301, 501).
        """
        self.players = {player: mode for player in players}
        self.mode = mode
        self.current_player_index = 0
        self.winner = None

    def throw(self, points):
        """
        Verarbeitet einen Wurf des aktuellen Spielers.
        :param points: Punkte des Wurfs.
        """
        current_player = self.get_current_player()
        if points <= self.players[current_player]:
            self.players[current_player] -= points
            if self.players[current_player] == 0:
                self.winner = current_player
        self.next_turn()

    def next_turn(self):
        """Wechselt zum nÃ¤chsten Spieler."""
        if self.winner is None:
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def get_current_player(self):
        """Gibt den Namen des aktuellen Spielers zurÃ¼ck."""
        return list(self.players.keys())[self.current_player_index]

    def get_scores(self):
        """Gibt die PunktestÃ¤nde aller Spieler zurÃ¼ck."""
        return self.players
