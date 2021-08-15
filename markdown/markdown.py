import re

formats = [
        ( '(.*?)__(.*?)__(.*?)' ,       r'\g<1><strong>\g<2></strong>\g<3>' ),
        ( '(.*?)_(.*?)_(.*?)' ,         r'\g<1><em>\g<2></em>\g<3>' ),
        ( r'(?m)^([^\*#].*)' ,          r'<p>\g<1></p>' ),
        ( r'(?m)^\* (.*)$' ,            r'<li>\g<1></li>' ),
        ( r'(?m)(((^<li>.*$)\n?)+)' ,   r'<ul>\g<1></ul>')
        ] 

# construct additional regex formats for each heading type
formats += [('(?m)^' + ('#'*n) + ' (.*)$', f'<h{n}>\\g<1></h{n}>') for n in range(1, 7)]

def parse(markdown):
    for (pattern, repl) in formats:
        markdown = re.sub(pattern, repl, markdown)
    
    return markdown.replace('\n', '')
