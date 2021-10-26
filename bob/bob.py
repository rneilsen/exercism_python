def response(hey_bob):
    cleaned = hey_bob.strip()
    
    if len(cleaned) == 0:
        # Catch empty strings first
        return "Fine. Be that way!"

    question = cleaned[-1] == '?'
    yelling = cleaned.isupper()

    if question and yelling:
        return "Calm down, I know what I'm doing!"
    if question:
        return "Sure." 
    if yelling:
        return "Whoa, chill out!"
    return "Whatever."

