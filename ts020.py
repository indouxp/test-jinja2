
from jinja2 import Template, Environment, FileSystemLoader
 
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('ts020.tpl')
 
data = {'name': 'Kuro', 'lang': 'Python'}
disp_text = template.render(data) # 辞書で指定する
print(disp_text)
