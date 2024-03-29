# All required modules in one place to be imported in other files.
import os
import json
import  shutil
import json
import requests
import re
import getpass
import pwinput
import tiktoken
import openai
from github import Github
from rich import print, pretty
pretty.install()


#files with this extensions are downloaded and sent for analyzing to ChatGPT
allowed_extensions = ['c', 'h', 'cpp', 'hpp', 'java', 'py', 'html', 'css', 'js', 'php', 'ruby', 'swift', 'go', 'dart', 'kotlin', 'ts', 'tsx', 'csharp', 'vb', 'scala', 'r', 'rust', 'lua', 'shell', 'sh', 'bash', 'ps1', 'json', 'xml', 'yaml', 'toml', 'ini']

# prompt_text="Analyze the following code and give suggestion for Code Improvement,Code Optimization,Bug Identification and Resolution, suggest no more than 2-3 points per topic.\n\n"
prompt_text="Please review the code below and identify any syntax or logical errors, suggest ways to refactor and improve code quality, enhance performance, address security concerns, and bug identification & fix. Limit your response to 2-3 suggestion per field."

#Directory path where the repository files are downloaded
repo_path=f"{os.path.dirname(os.path.realpath(__file__))}\\repo-downloads"


# 3-D art to show when main.py is run
codebase_ASCII_ART=""" 

 ______  ______  _____   ______  ______  ______  ______  ______       ______  __   __  ______  __      __  __  ______  ______  ______    
/\  ___\/\  __ \/\  __-./\  ___\/\  == \/\  __ \/\  ___\/\  ___\     /\  __ \/\ "-.\ \/\  __ \/\ \    /\ \_\ \/\___  \/\  ___\/\  == \   
\ \ \___\ \ \/\ \ \ \/\ \ \  __\\  \  __<\ \  __ \ \___  \ \  __\     \ \  __ \ \ \-.  \ \  __ \ \ \___\ \____ \/_/  /_\ \  __\\\ \  __<   
 \ \_____\ \_____\ \____-\ \_____\ \_____\ \_\ \_\/\_____\ \_____\    \ \_\ \_\ \_\\"\_ \ \_\ \_\ \_____\/\_____\/\_____\ \_____\ \_\ \_\ 
  \/_____/\/_____/\/____/ \/_____/\/_____/\/_/\/_/\/_____/\/_____/     \/_/\/_/\/_/ \/_/\/_/\/_/\/_____/\/_____/\/_____/\/_____/\/_/ /_/ 
                                                                                                                                         

            
"""