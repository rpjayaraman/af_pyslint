import pyslang
import argparse
import re
'''
Try to address this issue: https://github.com/MikePopoloski/slang/issues/533
Maybe first take unused ** item first 
'''
def pyslint_argparse():
  # Create the parser
  parser = argparse.ArgumentParser()
  # Add an argument
  parser.add_argument('-t', '--test', type=str, required=True)
  # Parse the argument
  args = parser.parse_args()
  return args

args = pyslint_argparse()
inp_test_name = args.test
print("Now testing: " +inp_test_name)

#Check 2: Check for trailing white space
with open(inp_test_name, 'r') as file:
    lines = file.readlines()

for i, line in enumerate(lines, start=1):
#Spliting string and white space and endswith make sure it has trailing space
    if line.rstrip('\n').endswith(' '):
        print("Following line has a trailing whitespace")
        print(f"Line {i}: {line.rstrip()}")

tree = pyslang.SyntaxTree.fromFile(inp_test_name)
mod = tree.root.members[0]
for scope_i in (tree.root.members):
  if(scope_i.kind.name != "ClassDeclaration"):
    print("Module name is: " + scope_i.header.name.value)
    if(scope_i.header.name.value != inp_test_name):
      print("FAIL, Test name is "+inp_test_name + " Recommended Test name -> af_"+ scope_i.header.name.value +'.'+"sv")
  else:
    if(scope_i.name.value != inp_test_name):
      print("Class name is: " + scope_i.name.value)
      print("FAIL, Test name is "+inp_test_name + " Recommended Test name -> af_"+ scope_i.name.value +'.'+"sv")
