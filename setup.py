from setuptools import find_packages, setup
from typing import List
#find ackages are used to find overall packages available w
#within machin elarning application. 
HYPHEN_DOT =  "-e ."

requirements=[]
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    with open(file_path)  as file_obj:
        requirements  =  file_obj.readlines()
        requirements =  [req.replace("\n","") for req in requirements]
        
        if HYPHEN_DOT in requirements: 
            requirements.remove(HYPHEN_DOT)
        
    requirements
   

setup(  
    name='mlproject',
    version='0.0.1',
    author= 'hlgsagar',
    author_email= 'hlgsagar.1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)