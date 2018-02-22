import os

from jinja2 import Template


researches = []
page_path = os.getcwd() + '/static/pages'
files = os.listdir(page_path)

titles = []
for file in files:
    with open(page_path + '/' + file, 'r', encoding='utf-8') as f:
        f_ = f.read()
        title = f_[f_.find('title>')+6:f_.find('</title')]
        id_ = file[:-5]
        journal = f_[f_.find('journal">')+9:]
        journal = journal[:journal.find('<')]
        if title in titles:
            continue
        titles.append(title)
        researches.append({'id': id_, 'title': title, 'journal': journal})

with open(os.getcwd() + '/nature_.html', 'r') as f:
    template = Template(f.read())
    nature = template.render(researches=researches)

    with open(os.getcwd() + '/nature.html', 'w', encoding='utf-8') as wf:
        wf.write(nature)
