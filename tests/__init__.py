from pydocgenerator.pydoc import DocGen

# testing the docstring genertion using a sample funciton.
docgen = DocGen('../../tests/test1.py')
docgen.write_to_file()