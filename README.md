# DartPI
# 🎯 SteelDart Rechner

## 📜 Projektbeschreibung
SteelDart Rechner ist eine moderne Python-Anwendung, die Dart-Spielern dabei hilft, ihre Spiele zu organisieren und Statistiken zu verfolgen. Ob klassisches "301" oder "501", die benutzerfreundliche Oberfläche ermöglicht eine einfache Verwaltung von Spielern, Spielmodi und Statistiken. Ziel ist es, Dart-Fans ein digitales Werkzeug an die Hand zu geben, um ihre Spiele effizient und unterhaltsam zu gestalten.

---

## 🎯 Ziele des Projekts
- **✨ Spielerlebnis verbessern**: Dart-Spiele digital und übersichtlich verwalten.
- **📊 Statistiken verfolgen**: Historische Daten speichern, um Fortschritte zu analysieren.
- **🔧 Erweiterbarkeit fördern**: Zusätzliche Spielmodi und Funktionen einfach hinzufügen können.

---

## 🛠️ Funktionen
- **👤 Spielerverwaltung**: Spieler können hinzugefügt und in einer Liste angezeigt werden.
- **🎮 Spielmodi**: Unterstützt klassische Modi wie "301" und "501" (mit Erweiterungsmöglichkeiten).
- **📈 Statistikverwaltung**: Automatische Speicherung und Anzeige von Spielstatistiken.
- **💻 Benutzerfreundliche GUI**: Klare und einfache Bedienung mit intuitiven Buttons und Eingabefeldern.

---

## 📥 Installation
### Voraussetzungen
- 🐍 Python 3.10 oder neuer
- 📦 Pip (Python-Paketmanager)
- 📂 SQLite3

### Schritte
1. **📂 Repository klonen**:
   ```bash
   git clone <repository-url>
   cd dart_rechner
   ```

2. **📦 Abhängigkeiten installieren**:
   ```bash
   pip install PySide6
   ```

3. **🗃️ Datenbank vorbereiten**:
   Die SQLite-Datenbank `dart_stats.db` wird automatisch beim ersten Start erstellt.

4. **🚀 Anwendung starten**:
   ```bash
   python3 main.py
   ```

---

## 🚀 Nutzung
1. **👤 Spieler hinzufügen**:
   - Gib den Namen eines Spielers ein und klicke auf "Hinzufügen".
2. **🎮 Neues Spiel starten**:
   - Wähle Spieler aus der Liste aus und starte ein neues Spiel.
3. **🎯 Würfe eingeben**:
   - Gib die Punkte eines Wurfs ein, und sie werden vom aktuellen Punktestand abgezogen.
4. **📊 Statistiken anzeigen**:
   - Klicke auf "Statistiken anzeigen", um vergangene Spielergebnisse einzusehen.

---

## 🗂️ Projektstruktur
```
.
├── database.py        # Datenbankoperationen
├── game_logic.py      # Spielmodi-Logik
├── gui.py             # Benutzeroberfläche
├── main.py            # Startpunkt der Anwendung
├── dart_stats.db      # SQLite-Datenbank (wird erstellt, falls nicht vorhanden)
└── README.md          # Projektdokumentation
```

---

## 📈 Nächste Schritte
- 🎯 Weitere Spielmodi wie "Cricket" implementieren.
- 📂 Statistiken exportieren (CSV-Format).
- 🎨 Modernes GUI-Design (Farben, Layouts) einfügen.

---

## 🤝 Mitwirken
Pull Requests sind willkommen! Bitte stelle sicher, dass du vorher ein Issue eröffnest, um größere Änderungen zu besprechen.

---

## 📝 Lizenz
Dieses Projekt ist unter der MIT-Lizenz veröffentlicht. Weitere Informationen findest du in der Datei `LICENSE`.

