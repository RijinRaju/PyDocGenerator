# PyDocGenerator
PyDocGenerator is a Python library that automatically generates docstrings for Python functions. It takes a Python file as input, generates docstrings for each function in the file, and outputs a new Python file with the generated docstrings.
# Features
 * Automatically generate docstrings for Python functions
 * Easy to use: just pass the file name to the DocGen instance and call the write_to_file() method
# Installation
You can install PyDocGenerator by cloning the repository or using pip:
      git clone [<repository-url>](https://github.com/RijinRaju/PyDocGenerator/) 

## Dependencies
- **transformers**: A library for natural language processing using pre-trained models.
    pip install transformers

- **torch**: The PyTorch library for deep learning and neural networks.
    pip install torch

- **astunparse**: A Python library for parsing and un-parsing abstract syntax trees (ASTs).
    pip install astunparse
  


# Usage
Here’s a simple example of how to use DocGen-AI:
```python 
  from pydocgenerator.pydoc import PyDOC

  py_doc = PyDOC('./filename.py')
  py_doc.write_to_file()
```
In this example, DocGen is instantiated with the path to a Python file ('./filename.py'). The write_to_file() method is then called to generate docstrings for each function in the file and output a new Python file with docstrings attached.

# License
DocGen-AI is licensed under the MIT License. See the LICENSE file for more information.