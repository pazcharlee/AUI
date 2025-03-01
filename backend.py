#import nbformat
##import os
#from Budgetly import handle_login, security_question



# Convert Jupyter Notebook to a Python script dynamically
#def load_notebook(notebook_path):
 #   with open(notebook_path, "r", encoding="utf-8") as nb_file:
 #       notebook = nbformat.read(nb_file, as_version=4)
  #      exporter = PythonExporter()
 #       python_script, _ = exporter.from_notebook_node(notebook)
#
 #   script_path = "Budgelty.py"  # Save as a Python script
 #   with open(script_path, "w", encoding="utf-8") as py_file:
 #       py_file.write(python_script)
 #   
 #   return script_path
#
#notebook_path = r"C:\Users\charl\AUI\Budgelty.ipynb"  # Absolute path

#script_path = load_notebook(notebook_path)

# Import functions from converted script
#if os.path.exists(script_path):
#    from Budgelty import handle_login, security_question
#else:
#    print("Failed to load Budgelty notebook.")