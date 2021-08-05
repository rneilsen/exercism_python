GESTURES = {0:  'wink', 
            1:  'double blink',
            2:  'close your eyes',
            3:  'jump'}

def commands(number):
    handshake = []
    for n in GESTURES.keys():
        if (number // 2**n) % 2:
            handshake.append(GESTURES[n])
    if (number // 16) % 2:
        handshake.reverse()
    return handshake
