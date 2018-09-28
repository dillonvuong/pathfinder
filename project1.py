from pathlib import Path
import shutil
paths = []
loop_first = 0
interesting = []


def paths_in_dir_d (the_path: str) -> list:
    'prints out all the files in one directory'
    result = []
    path = Path(the_path)
    for file in path.iterdir():
        if file.is_file():
            result.append(file)
    return result


def paths_in_dir_r (the_path: str) -> list:
    'prints out all of the files in the directory given and its subdirectories'
    result = []
    path = Path(the_path)
    result.append(paths_in_dir_d (the_path))
    for file in path.iterdir():
        if file.is_dir():
            result.extend(paths_in_dir_r(file))
    return result

#########################

def one_list (list_of_files: 'nested list of paths') -> list:
    'takes a nested list of lists and makes one list'
    for file in list_of_files:
        paths.extend(file)
    return(paths)

def print_out_list ( file_list: list ) -> str:
    'prints out a list of files, one on each newline'
    for file in file_list:
        print(file)

    
def is_text (file: Path) -> bool:
    'returns True if a file is a text file'
    try:
        content = open(file, 'r')
        content.readlines()
        return True
    except:
        return False
    
##########################

def choose() -> list:
    """executes the second part of the program
       where the user must input a command to
       determine interesting files"""
    loop_second = 0
    while loop_second == 0:
        
        choice = input()
        
        if choice == 'A':
            A(choice)
            loop_second = 1
            
        elif choice[0:2] == 'N ':
            N(choice)
            loop_second = 1
            
        elif choice[0:2] == 'E ':
            E(choice)
            loop_second = 1
            
        elif choice[0:2] == 'T ':
            T(choice)
            loop_second = 1
            
        elif choice[0:2] == '< ':
            less(choice)
            loop_second = 1
            
        elif choice[0:2] == '> ':
            greater(choice)
            loop_second = 1
            
        else:
            print('ERROR')
            
    return interesting


def choose2( files: list ) -> list:
    """ exectues the third part of the program
        where the user must input a command to
        act on the interesting files"""
    loop_last = 0
    while loop_last == 0:

        choice = input()

        if choice == 'F':
            for file in files:
                if is_text(file):
                    content = open(file, 'r')
                    print(content.readline().strip('\n'))
                else:
                    print('NOT TEXT')
            loop_last = 1
            
        elif choice == 'D':
            for file in files:
                shutil.copy(file, str(file.as_posix()) + '.dup')
            
            loop_last = 1
            
        elif choice == 'T':
            for file in files:
                file.touch()
            loop_last = 1 
            
        else:
            print('ERROR')
        
##########################
            
def A ( choice: str ) -> list:
    'returns all files'
    for file in paths:
        interesting.append(file)
    
    
        
def N ( choice: str ) -> list:
    'search for files with a particular name' 
    for file in paths:
        if file.name == choice.strip('N '):
            interesting.append(file)

def E (  choice: str  ) -> list:
    'search for files with a particular extension'
    for file in paths:
        if file.suffix == choice.strip('E '):
            interesting.append(file)
        elif file.suffix.strip('.') == choice.strip('E .'):
            interesting.append(file)
            
def T ( choice: str ) -> list:
    'search for text files containing a particular phrase'
    for file in paths:
        if is_text(file):
            content =  open(file, 'r')
            for line in content:
                if choice.strip('T ') in line:
                    interesting.append(file)
            content.close()

def less ( choice: str ) -> list:
    'search for files with less bytes than input'
    for file in paths:
        if file.stat().st_size < int(choice.strip('< ')):
            interesting.append(file)

def greater ( choice: str ) -> list:
    'search for files with greater bytes than input'
    for file in paths:
        if file.stat().st_size > int(choice.strip('> ')):
            interesting.append(file)
            
##########################
            
while loop_first == 0:
    
    userinput = input()
    
    try:
        
        if userinput[0:2] == 'D ':
            path = userinput.strip('D ')
            paths = paths_in_dir_d(path)
            print_out_list((paths_in_dir_d(path)))
            loop_first = 1
            print_out_list(choose())
            choose2(interesting)
                    
        elif userinput[0:2] == 'R ':
            path = userinput.strip('R ')
            print_out_list(one_list((paths_in_dir_r(path))))
            loop_first = 1
            print_out_list(choose())
            choose2(interesting)

                
        else:
            print('ERROR')
            
    except:
        print('ERROR')




