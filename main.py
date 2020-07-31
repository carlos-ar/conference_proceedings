#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:01:01 2020

@author: carlosar
"""

import os
import shutil
import jinja2
import pandas as pd

def delete_files(folder): 
    # https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder
    # folder = '/path/to/folder'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

input_abs = pd.read_excel('input_abstracts.xlsx')
abstract_fnames = input_abs.abstract_name

latex_jinja_env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    comment_start_string = '\#{',
    comment_end_string = '}',
    line_statement_prefix = '%-',
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(os.path.abspath('.'))
    )
# load template files from template directory 
abs_template = latex_jinja_env.get_template('./templates/abstract.tex')
main_template = latex_jinja_env.get_template('./templates/main-template.tex')



# delete subfiles if they exist:
delete_files('./texsrc')
# https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
for index, row in input_abs.iterrows():
    #print(row)
    # make individual abstracts
    abstract = abs_template.render(title=row.abstract_name,
                                   author_firstname=row.author_firstname,
                                   author_lastname=row.author_lastname,
                                   advisor_firstname=row.advisor_firstname,
                                   advisor_lastname=row.advisor_lastname,
                                   advisor_titles=row.advisor_titles,
                                   co_authors=row.author_lastname,
                                   abstract=row.abstract_text)
    
    # write abstract files
    abs_fname = os.path.join('./texsrc', row.abstract_name+'.tex')
    with open(abs_fname,'w') as output:
        output.write(abstract)

# make main tex file
main = main_template.render(abstracts = abstract_fnames)
with open('./main.tex','w') as output:
    output.write(main)    
