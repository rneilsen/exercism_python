# NOTE: Define divisors and corresponding raindrop sounds here
RAINDROPS = {
    3: "Pling",
    5: "Plang",
    7: "Plong"
}

def convert(number):
    output = ""

    # Iterate through divisors and append sounds for each that divides 'number'
    for div in RAINDROPS:
        if number % div == 0:
            output += RAINDROPS[div]
    
    return(output if output != "" else str(number))
