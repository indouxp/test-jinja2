#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Template

tpl_text = "名前:{{ name }}。 言語は{{ lang }}。"
template = Template(tpl_text)

data = {'name': '黒', 'lang': 'python'}
disp_text = template.render(data)
print(disp_text)
