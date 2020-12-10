GIFTS = (None, "a Partridge in a Pear Tree", "two Turtle Doves", 
         "three French Hens", "four Calling Birds", "five Gold Rings",
         "six Geese-a-Laying", "seven Swans-a-Swimming", 
         "eight Maids-a-Milking", "nine Ladies Dancing", 
         "ten Lords-a-Leaping", "eleven Pipers Piping", 
         "twelve Drummers Drumming")

ORDS = (None, "first", "second", "third", "fourth", "fifth", "sixth", 
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth")


def verse(n: int) -> str:
    return (f"On the {ORDS[n]} day of Christmas my true love gave to me: " +
            ', '.join([GIFTS[i] for i in range(n, 1, -1)]) +
            (', and ' if n > 1 else '') + GIFTS[1] + '.')


def recite(start_verse: int, end_verse: int) -> list:
    return [verse(n) for n in range(start_verse, end_verse + 1)]
