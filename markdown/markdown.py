import re


blocks = [re.compile('(.*)__(.*?)__(.*)')]


def parse(markdown):
    lines = markdown.splitlines()
    res_lines = []
    in_list = False
    end_list = False
    for line in lines:
        in_para = True  # assume all lines are para until detect list or heading

        # Detect headings
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
                in_list = False
                end_list = True

        if in_para:
            line = '<p>' + line + '</p>'
        
        if end_list:
            line = '</ul>' + line
            end_list = False

        res_lines.append(line)

    if in_list:
        res_lines.append('</ul>')
    return ''.join(res_lines)
