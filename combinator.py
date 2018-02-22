import os
from datetime import datetime

from jinja2 import Template


researches = {}
page_path = os.getcwd() + '/static/pages'
files = os.listdir(page_path)

for file in files:
    with open(page_path + '/' + file, 'r', encoding='utf-8') as f:
        f_ = f.read()
        title = f_[f_.find('title>')+6:f_.find('</title')]
        id_ = file[:-5]
        journal = f_[f_.find('journal">')+9:]
        journal = journal[:journal.find('<')]

        if journal not in researches:
            researches[journal] = [{'id': id_,
                                    'title': title,
                                    'journal': journal}]
        else:
            researches[journal].append({'id': id_,
                                        'title': title,
                                        'journal': journal})

with open(os.getcwd() + '/nature_.html', 'r') as f:
    template = Template(f.read())
    date = datetime.now()
    author = '唼喋'
    nature = template.render(researches=researches, date=date, author=author)

    with open(os.getcwd() + '/nature.html', 'w', encoding='utf-8') as wf:
        wf.write(nature)
