#!/usr/bin/env python

from distutils.core import setup

setup(name='covid',
      version='1.0',
      description='COVID case/death mandate integrator',
      author='Jee Hoon Han, Oliver Li, Zhaowen Guo, Gabriel Wisswaesser',
      author_email='',
      url='https://github.com/gabewiss/covid',
      packages=['datetime', 'json', 'urllib', 'dash', 'pandas',
                'plotly.express', 'plotly.graph_objects',
                'plotly.graph_objs.scatter.marker', 'dash_core_components',
                'dash_html_components', 'dash.dependencies',
                'jupyter_dash'])
