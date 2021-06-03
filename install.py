#!python3
import os 
import subprocess
from os.path import join
from pathlib import Path
home_dir = str(Path.home())
proj_dir = join( home_dir ,'1m','apps')
git_org = 'git@github.com:psytron/'



# CREATE SYMLINK FOR DEV DIRS
def link_repo( proj_name ):
    os.chdir( proj_dir )
    target_path = join( proj_dir , proj_name )
    if os.path.isfile( target_path ) :
        os.symlink( targ_path, proj_name, True )


# CLONE REPOS FROM GITHUB TO PROJDIR 
def clone_repo( proj_name ):
    target_path = join( proj_dir , proj_name )
    os.chdir( target_path )
    if not os.path.isfile( target_path ):
        try:
            subprocess.Popen(['git', 'clone', git_org + proj_name + ".git"] )
        except Exception as e:
            print( e )


# BIND DEPENDENCIES TO LOCAL CLONES 
deps = [ 'space', 'blobrouter' ]
[ clone_repo(x) for x in deps ]
[ link_repo(x) for x in deps ]