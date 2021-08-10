import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for line in lines:
        # Detect headers
        m = re.match('(#+) (.*)', line)
        if m:
            ht = str(len(m.group(1)))
            line = f'<h{ht}>' + m.group(2) + f'</h{ht}>'

        # Detect bold
        while m := re.match('(.*)__(.*?)__(.*)', line):
            line = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        
        # Detect italic
        while m := re.match('(.*)_(.*?)_(.*)', line):
            line = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        
        m = re.match(r'\* (.*)', line)
        if m:
            if not in_list:
                in_list = True
                curr = m.group(1)
                line = '<ul><li>' + curr + '</li>'
            else:
                curr = m.group(1)
                line = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', line)
        if not m:
            line = '<p>' + line + '</p>'
        
        if in_list_append:
            line = '</ul>' + line
            in_list_append = False
        res += line
    if in_list:
        res += '</ul>'
    return res