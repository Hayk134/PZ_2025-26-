import sqlite3

conn = sqlite3.connect("rent.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS points (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    floor INTEGER,
    area REAL,
    conditioner TEXT,
    price REAL
)
""")

cur.execute("SELECT COUNT(*) FROM points")
if cur.fetchone()[0] == 0:
    data = [
        (1, 50.0, "да", 1500), (1, 30.0, "нет", 900),
        (2, 75.0, "да", 2200), (2, 20.0, "нет", 700),
        (3, 120.0, "да", 4000), (3, 45.0, "нет", 1100),
        (1, 85.0, "да", 2500), (4, 60.0, "нет", 1300),
        (2, 40.0, "да", 1400), (3, 15.0, "нет", 500)
    ]
    cur.executemany("INSERT INTO points (floor, area, conditioner, price) VALUES (?, ?, ?, ?)", data)
    conn.commit()

cur.execute("SELECT * FROM points WHERE floor = 1")
print(cur.fetchall())

cur.execute("SELECT * FROM points WHERE area > 50")
print(cur.fetchall())

cur.execute("SELECT * FROM points WHERE conditioner = 'да'")
print(cur.fetchall())

cur.execute("UPDATE points SET price = price + 100 WHERE floor = 3")
cur.execute("UPDATE points SET conditioner = 'да' WHERE area > 100")
cur.execute("UPDATE points SET price = price * 0.9 WHERE conditioner = 'нет'")
conn.commit()

cur.execute("DELETE FROM points WHERE price < 600")
cur.execute("DELETE FROM points WHERE floor = 4")
cur.execute("DELETE FROM points WHERE area < 20 AND conditioner = 'нет'")
conn.commit()

cur.execute("SELECT * FROM points")
for row in cur.fetchall():
    print(row)

conn.close()