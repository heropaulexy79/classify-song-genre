# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 17:02:27 2023

@author: USER
"""

import streamlit as st
import subprocess

def run_jupyter_notebook(notebook_path):
    cmd = f"jupyter nbconvert --execute --to notebook --inplace {notebook_path}"
    subprocess.call(cmd, shell=True)
    
notebook_path = r'C:\Users\USER\Desktop\Python apps\workspace\workspace'

run_jupyter_notebook(notebook_path)

def convert_to_streamlit(notebook_path):
    cmd = f"jupyter nbconvert --to python {notebook_path}"
    subprocess.call(cmd, shell=True)

convert_to_streamlit(notebook_path)

