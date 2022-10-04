print(*(lambda random: (random.randint(163, 190) for _ in range(12)))(__import__("random")))
