# MD_Doc_Gen

MD Documentation Generator.

It generates an .md file with every function that is documented, in each directory of the current project.

## Pre-Conditions:

- Works only with python files
- The sintax for the documentation should start and end with `"""`

Example:
```python
def functions(par)-> returnType:
    """Descriptions stuff
    	Args:
    		arg0(type): descriptions 
    	Another Title:
    		... 
    	Returns:
    		...
    """
```
