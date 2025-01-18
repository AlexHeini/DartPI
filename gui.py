from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QLabel, QWidget
from database import add_player, get_players, save_game_result, get_statistics
from game_logic import Game

class DartApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SteelDart Rechner")
        self.setGeometry(100, 100, 800, 600)
        self.game = None  # Initialisiere das Spiel-Objekt
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Spieler hinzufÃ¼gen
        self.label = QLabel("Spieler hinzufÃ¼gen:")
        self.player_input = QLineEdit()
        self.add_button = QPushButton("HinzufÃ¼gen")
        self.add_button.clicked.connect(self.add_player)

        # Spielerliste
        self.players_label = QLabel("Spielerliste:")
        self.players_list = QLabel()

        # Neues Spiel starten
        self.new_game_button = QPushButton("Neues Spiel starten")
        self.new_game_button.clicked.connect(self.start_new_game)

        # Punkte eingeben
        self.throw_input = QLineEdit()
        self.throw_input.setPlaceholderText("Punkte eingeben...")
        self.throw_button = QPushButton("Wurf ausfÃ¼hren")
        self.throw_button.clicked.connect(self.process_throw_input)

        # Statistiken anzeigen
        self.stats_button = QPushButton("Statistiken anzeigen")
        self.stats_button.clicked.connect(self.show_statistics)

        # Layout hinzufÃ¼gen
        layout.addWidget(self.label)
        layout.addWidget(self.player_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.players_label)
        layout.addWidget(self.players_list)
        layout.addWidget(self.new_game_button)
        layout.addWidget(self.throw_input)
        layout.addWidget(self.throw_button)
        layout.addWidget(self.stats_button)

        # Setze das Layout in das Hauptfenster
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_player(self):
        """FÃ¼gt einen neuen Spieler hinzu und aktualisiert die Spielerliste."""
        name = self.player_input.text()
        if name:
            add_player(name)
            self.update_players_list()
            self.player_input.clear()

    def update_players_list(self):
        """Aktualisiert die Spielerliste in der GUI."""
        players = get_players()
        self.players_list.setText("\n".join([f"{p[0]}: {p[1]}" for p in players]))

    def start_new_game(self):
        """Startet ein neues Spiel mit den vorhandenen Spielern."""
        players = [player[1] for player in get_players()]
        if players:
            self.game = Game(players)
            self.update_scores()
        else:
            self.players_list.setText("Keine Spieler vorhanden!")

    def update_scores(self):
        """Aktualisiert die PunktestÃ¤nde in der GUI."""
        if self.game:
            scores = self.game.get_scores()
            score_text = "\n".join([f"{player}: {score}" for player, score in scores.items()])
            self.players_list.setText(score_text)

    def process_throw_input(self):
        """Liest die Punkte aus der Eingabe und verarbeitet den Wurf."""
        try:
            points = int(self.throw_input.text())
            self.process_throw(points)
            self.throw_input.clear()
        except ValueError:
            self.players_list.setText("UngÃ¼ltige Punkteingabe!")

    def process_throw(self, points):
        """Verarbeitet einen Wurf."""
        if self.game:
            self.game.throw(points)
            self.update_scores()
            if self.game.winner:
                self.players_list.setText(f"Gewinner: {self.game.winner}")
                # Gewinner-ID abrufen
                players = get_players()
                for player in players:
                    if player[1] == self.game.winner:
                        save_game_result(player[0], self.game.mode, 0)  # Punkte = 0 bei Sieg

    def show_statistics(self):
        """Zeigt alle gespeicherten Statistiken in der GUI an."""
        stats = get_statistics()
        if stats:
            stats_text = "\n".join([f"{row[0]} | {row[1]} | {row[2]} Punkte | {row[3]}" for row in stats])
            self.players_list.setText(f"Statistiken:\n{stats_text}")
        else:
            self.players_list.setText("Keine Statistiken verfÃ¼gbar.")

if __name__ == "__main__":
    app = QApplication([])
    window = DartApp()
    window.show()
    app.exec()

