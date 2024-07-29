# report_generator.py
import os
import json
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

# Directories for folders
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
FILE_DIR = os.path.join(BASE_DIR, 'files')

# Directories for input and output
JSON_NAME = 'changes.json'
HTML_NAME = 'report_template.html'
JSON_DIR = os.path.join(FILE_DIR, JSON_NAME)
HTML_DIR = os.path.join(FILE_DIR, HTML_NAME)
HTML_FILE_OUT = os.path.join(FILE_DIR, 'output.html')
PDF_FILE_OUT = os.path.join(FILE_DIR, 'output.pdf')

# Load JSON data
with open(JSON_DIR) as f:
    changes = json.load(f)

# Ascertaining the number of changes by category
n_insert = len(changes.get('insert'))
n_delete = len(changes.get('delete'))
n_replace = len(changes.get('replace'))

# Set up Jinja2 environment
## FileSystemLoader -> directory containing your templates
env = Environment(loader=FileSystemLoader(FILE_DIR))
template = env.get_template(HTML_NAME)

# Render HTML with JSON data
html_out = template.render(insert=changes.get('insert'), 
                           delete=changes.get('delete'), 
                           replace=changes.get('replace'), 
                           n_insert=n_insert, 
                           n_delete=n_delete, 
                           n_replace=n_replace)


# Write html file
with open(HTML_FILE_OUT, 'w') as f:
    f.write(html_out)
    
# Convert HTML to PDF with WeasyPrint
HTML(HTML_FILE_OUT).write_pdf(PDF_FILE_OUT) 

breakpoint()