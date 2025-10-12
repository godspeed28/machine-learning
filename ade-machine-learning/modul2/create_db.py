import sqlite3

# Buat atau buka database baru
conn = sqlite3.connect("data/classic_rock.db")

# Buat cursor untuk eksekusi SQL
cursor = conn.cursor()

# Buat tabel rock_songs
cursor.execute("""
CREATE TABLE IF NOT EXISTS rock_songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    artist TEXT,
    album TEXT,
    year INTEGER
)
""")

# Tambahkan beberapa data contoh
songs = [
    ("Stairway to Heaven", "Led Zeppelin", "Led Zeppelin IV", 1971),
    ("Bohemian Rhapsody", "Queen", "A Night at the Opera", 1975),
    ("Hotel California", "Eagles", "Hotel California", 1976),
    ("Smoke on the Water", "Deep Purple", "Machine Head", 1972),
    ("Sweet Child O' Mine", "Guns N' Roses", "Appetite for Destruction", 1987)
]

cursor.executemany("INSERT INTO rock_songs (title, artist, album, year) VALUES (?, ?, ?, ?)", songs)

# Simpan perubahan dan tutup koneksi
conn.commit()
conn.close()

print("✅ Database classic_rock.db berhasil dibuat!")
