import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for line in lines:
        in_para = True  # assume all lines are para until detect list or header

        # Detect headers
        if ( m := re.match('(#+) (.*)', line) ):
            in_para = False
            ht = str(len(m.group(1)))
            line = f'<h{ht}>' + m.group(2) + f'</h{ht}>'

        # Detect bold
        while ( m := re.match('(.*)__(.*?)__(.*)', line) ):
            line = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        
        # Detect italic
        while ( m := re.match('(.*)_(.*?)_(.*)', line) ):
            line = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        
        # Detect list items
        if ( m := re.match(r'\* (.*)', line) ):
            in_para = False
            line = '<li>' + m.group(1) + '</li>'
            if not in_list:
                in_list = True
                line = '<ul>' + line
        elif in_list:
                in_list_append = True
                in_list = False

        if in_para:
            line = '<p>' + line + '</p>'
        
        if in_list_append:
            line = '</ul>' + line
            in_list_append = False
        res += line

    if in_list:
        res += '</ul>'
    return res

parse("# Start a list\n* Item 1\n* Item 2\nEnd a list"),