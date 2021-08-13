import re

formats = [
        (r'(.*?)__(.*?)__(.*?)', r'\g<1><strong>\g<2></strong>\g<3>'),
        (r'(.*?)_(.*?)_(.*?)', r'\g<1><em>\g<2></em>\g<3>'),
        ]

def parse(markdown):
    # sub all formatting blocks like bold and italics
    for (pattern, repl) in formats:
        markdown = re.sub(pattern, repl, markdown)

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
