# True love gift from each day of Christmas
DAYS = { 1: "a Partridge in a Pear Tree",
         2: "two Turtle Doves",
         3: "three French Hens",
         4: "four Calling Birds",
         5: "five Gold Rings",
         6: "six Geese-a-Laying",
         7: "seven Swans-a-Swimming",
         8: "eight Maids-a-Milking",
         9: "nine Ladies Dancing",
        10: "ten Lords-a-Leaping",
        11: "eleven Pipers Piping",
        12: "twelve Drummers Drumming"}

# Ordinal number names for each day of Christmas
ORDS = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 
        6: "sixth", 7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth", 
        11: "eleventh", 12: "twelfth"}


def verse(n):
    # returns a string containing a specific day's verse
    return (f"On the {ORDS[n]} day of Christmas my true love gave to me: " +
            ', '.join([DAYS[i] for i in range(n, 1, -1)]) +
            (', and ' if n > 1 else '') + DAYS[1] + '.')


def recite(start_verse, end_verse):
    # returns a list containing all verses from start_verse to end_verse
    return [verse(n) for n in range(start_verse, end_verse + 1)]
