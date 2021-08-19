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
            raise ValueError("Invalid format")
        if  ( pieces[1] in ops.values()
                and pieces[0].lstrip('-').isnumeric() 
                and pieces[2].lstrip('-').isnumeric() ) :
            pieces = [str(eval(''.join(pieces[0:3])))] + pieces[3:]
        else:    
            raise ValueError("Invalid format")

    return int(pieces[0])
