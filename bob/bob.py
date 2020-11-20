def response(hey_bob):
    cleaned = hey_bob.strip()
    (question, yelling) = (False, False)
    
    if len(cleaned) == 0:
        # Catch empty strings first
        return "Fine. Be that way!"

    if cleaned[-1] == '?':
        question = True
    if cleaned.isupper():
        yelling = True

    if question and yelling:
        return "Calm down, I know what I'm doing!"
    elif question:
        return "Sure." 
    elif yelling:
        return "Whoa, chill out!"
    else: 
        return "Whatever."

