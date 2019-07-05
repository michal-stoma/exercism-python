def convert(number):
    FACTORS = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'
    }

    sound = [FACTORS[factor] for factor in sorted(FACTORS)
             if number % factor == 0]

    return ''.join(sound) or str(number)
