import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"

import git
from git import Repo

def clone_repo(gitUrl,repoDirectory ):
    
    Repo.clone_from(gitUrl, repoDirectory)   # cloning the repo 
    
    print( f"the  repo  is cloned !!!!! and it  saved in the location {repoDirectory}")
    
    return f"{repoDirectory} "
    

gitUrl = "https://github.com/PhonePe/pulse"
repoDirectory = "D:\phone_pay_data"
clone_repo(gitUrl,repoDirectory)

