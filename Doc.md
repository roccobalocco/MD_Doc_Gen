## Directory MD_DOC_GEN 

 ### File generateDoc.py 

 

 ### Function Header --> 

`getDoc(body: list)-> str:
    ` 

 - Obtain the body of the documentation
- Args:
  - body (list): row of a function
- Returns:
  - str: body of the documentation


 ### Function Header --> 

`scanFile(fName: str, dirName: str)-> str:
    ` 

 - Obtain the documentation of a given file
- Args:
  - fName (str): name of the file to scan
  - dirName (str): name of the directory where the file is located
- Returns:
  - str: functions documentation


 ### Function Header --> 

`getDocumentation(files: list, d: str)-> str:
    ` 

 - Obtain the documentation of the functions from a given file list
- Args:
  - files (list): list of files to search for documentation
  - d (str): name of the directory where files are
- Returns:
  - str: documentation


 ### Function Header --> 

`getFileList(dir: str)-> list:
    ` 

 - Generate file list from a directory
- Args:
  - dir (str): directory to scan and get files
- Returns:
  - list: list of file names from the directory
 

 <hr> 

