import sqlite3

DB_PATH = "dart_stats.db"

def create_connection():
    """Verbindung zur SQLite-Datenbank herstellen."""
    conn = sqlite3.connect(DB_PATH)
    return conn

def add_player(name):
    """FÃ¼gt einen neuen Spieler zur Datenbank hinzu."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO spieler (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_players():
    """Liest alle Spieler aus der Datenbank aus."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM spieler")
    players = cursor.fetchall()
    conn.close()
    return players

def save_game_result(spieler_id, spielmodus, punkte):
    """
    Speichert das Ergebnis eines Spiels in der Statistik-Tabelle.
    :param spieler_id: ID des Spielers
    :param spielmodus: Modus des Spiels (z. B. "301", "501")
    :param punkte: Erzielte Punkte
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO statistik (spieler_id, spielmodus, punkte)
        VALUES (?, ?, ?)
    """, (spieler_id, spielmodus, punkte))
    conn.commit()
    conn.close()

def get_statistics():
    """
    Ruft alle Statistiken aus der Datenbank ab.
    :return: Liste der Statistiken
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT spieler.name, statistik.spielmodus, statistik.punkte, statistik.datum
        FROM statistik
        JOIN spieler ON statistik.spieler_id = spieler.id
        ORDER BY statistik.datum DESC
    """)
    stats = cursor.fetchall()
    conn.close()
    return stats

