"""
File Organization
"""

# The dict "files" below contains file names and the name of the person who owns each file. Write and call a function to reorganize "files" such that it contains each person's name and the files he/she owns. Assign the resultant dict to a new dict called "grouped_by_owner". Print out the key value pairs in this format - key: value.

# Function name should be: group_by_owners
# Dict of results should be named: files_by_owner


def group_by_owners(files):
  owners = {}

  for k,v in files.items():
    if v not in owners.keys():
      owners.update({v:k})
    elif v in owners.keys():
      if isinstance(owners[v],list) == False:
        add_val = [owners[v]]
        add_val.append(k)
        owners.update({v:add_val})
      elif isinstance(owners[v],list) == True:
        add_val = owners[v]
        add_val.append(k)

  return owners

files = {
  'Input1.txt': 'Beau',
  'Code1.py': 'Mischa',
  'Output1.txt': 'Beau',
  'Input2.txt': 'Beau',
  'Code2.py': 'Mischa',
  'Output2.txt': 'Beau',
  'Input3.txt': 'Percy',
  'Code3.py': 'Alejandra',
  'Output3.txt': 'Percy'
}

files_by_owner = group_by_owners(files)

for k,v in files_by_owner.items():
  print(f'{k}: {files_by_owner[k]}')