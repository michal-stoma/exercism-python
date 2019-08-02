def convert(number):
    FACTORS = [
        (3, 'Pling'),
        (5, 'Plang'),
        (7, 'Plong')
    ]

    sound = [factor[1] for factor in FACTORS
             if number % factor[0] == 0]

    return ''.join(sound) or str(number)
