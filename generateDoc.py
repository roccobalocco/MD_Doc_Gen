import os
import sys
sys.path.insert(0, '..')

def getDoc(body: list)-> str:
    """Obtain the body of the documentation

    Args:
        body (list): row of a function

    Returns:
        str: body of the documentation
    """    
    s = ""
    toCut = 0
    for el in body:
        b = True
        for e in el.split('\n'):
            if b:
                s += "- " + e.strip() + "\n"
                b = False
                toCut = len(e.strip()) + 3
            else:
                s += "  - " + e.strip() + "\n"
                toCut = len(e.strip()) + 5
    return s[:-toCut]

def scanFile(fName: str, dirName: str)-> str:
    """Obtain the documentation of a given file

    Args:
        fName (str): name of the file to scan
        dirName (str): name of the directory where the file is located

    Returns:
        str: functions documentation
    """    
    f = open("../" + dirName + "/" + fName, "r")
    s = ""
    fileContent = f.read()

    for line in fileContent.split("def "):
        if line.__contains__("\"\"\""):
            line = line.split("\"\"\"")
            func, docs = line[0], line[1]
            s += "\n\n ### Function Header --> \n\n`" + func + "` \n\n "
            s += getDoc(docs.split("\n\n"))
        

    return s

def getDocumentation(files: list, d: str)-> str:
    """Obtain the documentation of the functions from a given file list

    Args:
        files (list): list of files to search for documentation
        d (str): name of the directory where files are

    Returns:
        str: documentation
    """    
    s = "## Directory " + d + " \n\n "
    for f in files:
        s += "### File " + f + " \n\n "
        s += scanFile(f, d)
        s += " \n\n <hr> \n\n"
    return s

def getFileList(dir: str)-> list:
    """Generate file list from a directory 

    Args:
        dir (str): directory to scan and get files

    Returns:
        list: list of file names from the directory
    """    
    l = list()
    for e in os.scandir('../' + dir):
        if e.name.__contains__('.py'):
            l.append(e.name)
    return l

#start of script:
#put this file in the utility directory if u have one, this way you don't have to modify nothing here
entries = os.scandir('../') #put the main directory into scandir
for e in entries:
    if e.is_dir() and not e.name.__contains__('.'):
        directory = e.name
        files = getFileList(directory)
        mdString = getDocumentation(files, directory)
        f = open("../" + directory + "/Doc.md", "w") # write file in each directory
        f.write(mdString)
        f.close()