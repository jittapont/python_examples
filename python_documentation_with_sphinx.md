# How to write python documentation with Sphinx

1.  Install Sphinx
```bash
  pip install Sphinx
```
2.  Create docs folder and go to docs folder
```bash
  mkdir docs
  cd docs
```
3.  Run sphinx quickstart (don't forget to separate source and build folder)
```bash
  sphinx-quickstart
```
4.  Edit docs config.py in docs/source folder
```python
  # docs/source/conf.py
  import os
  import sys
  sys.path.insert(0, os.path.abspath('../..')) # path to library
  
  # Add this extensions
  extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']
```
5.  Generate api docs from [**sphinx style docstring**](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)
```python
  # Example doc string
  """
  [Summary]

  :param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
  :type [ParamName]: [ParamType](, optional)
  ...
  :raises [ErrorType]: [ErrorDescription]
  ...
  :return: [ReturnDescription]
  :rtype: [ReturnType]
  """
```
```bash
  cd docs/
  sphinx-apidoc -o source/ ../<package name>
```
6.  Go to docs and clean build folder
```bash
  make clean
```
7.  Generate document
```bash
  make html
```
