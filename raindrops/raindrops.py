# NOTE: Define divisors and corresponding raindrop sounds here
RAINDROPS = {
    3: "Pling",
    5: "Plang",
    7: "Plong"
}

def convert(number):
    output = ""
    divisors = sorted([d for d in RAINDROPS.keys()])

    # Iterate through divisors and append sounds for each that divides 'number'
    for div in divisors:
        if number % div == 0:
            output += RAINDROPS[div]
    
    return(output if output != "" else str(number))
