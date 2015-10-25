import sqlite3
import matplotlib.pyplot as plt
from collections import defaultdict


def main():
    detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
    conn = sqlite3.connect("lots.db", detect_types=detect_types)
    c = conn.cursor()
    lots = defaultdict(lambda: ([], [],))
    sql = "SELECT created_at, name, free FROM free_lots ORDER BY created_at"

    for created_at, name, free in c.execute(sql):
        times, counts = lots[name]
        times.append(created_at)
        counts.append(free)

    for name, data in lots.items():
        plt.plot(data[0], data[1], label=name)
    plt.ylabel('Freie Parkplätze')
    plt.xlabel('Zeit')
    plt.legend(loc='upper left')
    plt.show()


if __name__ == "__main__":
    main()
