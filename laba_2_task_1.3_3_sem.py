def half_decay(t12):
    def dynamic(n0, t):
        n = n0 * (1/2)**(t/t12)
        return n
    return dynamic

isotops = {
    "I-131": half_decay(8.0),           # Йод-131 — 8 дней
    "Cs-137": half_decay(30.17),        # Цезий-137 — 30.17 лет
    "U-235": half_decay(703_800_000),   # Уран-235 — 703.8 млн лет
    "Ra-226": half_decay(1600),         # Радий-226 — 1600 лет
    "C-14": half_decay(5730),           # Углерод-14 — 5730 лет
    "Po-210": half_decay(138.4),        # Полоний-210 — 138.4 дней
}


n0 = 100
t = 20
for element, result in isotops.items():
    print(f" {element}, осталось: {result(n0, t)} дней")

