from re import sub

ops = { 'plus'          : '+' , 
        'minus'         : '-' ,
        'multiplied by' : '*' , 
        'divided by'    : '//' }

def answer(question):
    if not ( question.startswith('What is') and question[-1] == '?' ):
        raise ValueError("Invalid question format")
    
    for k,v in ops.items():
        question = sub(k, v, question)
    
    pieces = question[8:-1].split(' ')

    while len(pieces) > 1:
        if len(pieces) < 3:
            raise ValueError("Unknown question")
        
        pieces = [str(eval(''.join(pieces[0:3])))] + pieces[3:]

    return int(pieces[0])
    