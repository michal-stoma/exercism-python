def convert(number):
    FACTORS = [3, 5, 7]
    FACTORS_MAP = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'
    }

    sound = [FACTORS_MAP[factor] for factor in FACTORS if number % factor == 0]

    return ''.join(sound) or str(number)
