# PythonTraining

## Install Django Python Environment

Jump To:
* [Windows](#windows)  
* [Linux/Mac OS](#linuxmac-os)

### Windows

**Note:** For lines with multiple commands the first one is preferred, e.g. the `py -<version>`.  The other will only work if the python version you want to use is linked to the `python` command.

1. Go-to the python download page and download python 3.6
    1. https://www.python.org/downloads/
2. Run the installation tool. Make sure the "Add python to PATH" box is checked, and under advanced settings, make sure that the pip box is checked.
3. Confirm that the python version by running one of the following commands in an Administrator PowerShell window (Search for powershell, right click and run as administrator) The output should be “Python 3.6.x”
    1. `py -3.6 --version`
    2. `python --version`
4. Confirm that you have pip installed by running one of the following commands (the output should be `pip 9.0.1 from <path> (python 3.6)`)
    1. `py -3.6 -m pip --version`
    2. `python -m pip --version`
5. Install virtualenv from pip with one of the following commands
    1. `py -3.6 -m pip install virtualenv`
    2. `python -m pip install virtualenv`
6. Create a directory where you want your application source code to live (perhaps in your documents folder, on the desktop, or in the C:/ drive)
    1. `cd C:\`
    2. `mkdir sds_python`
    3. `cd C:\sds_python`
7. Create the virtual environment using one of the following commands
    1. `py -3.6 -m virtualenv <env_name>`
    2. `python -m virtualenv <env_name>`
8. Activate the virtual environment in your current shell from your source code directory (after activating “(<env_name>)” should appear in front of your terminal prompt)
    1. Powershell
        1. `.\<env_name>\Scripts\activate.ps1`
    2. Cmd
        1. `.\<env_name>\Scripts\activate.bat`
9. Confirm that python and pip are correctly linked
    1. Python
        1. Run `python --version`
        2. Should return `Python 3.6.x`
    2. Pip
        1. Run `pip --version`
        2. Should return `pip 9.0.1 from <path> (python 3.6)`
10. Install Django in the virtual env with the following command
    1. `pip install django`
11. Confirm that Django is correctly installed by running the following command (should return `2.0.1` or something similar)
    1. `python -m django --version`
12. To exit from the virtual environment execute `deactivate` to re-enter the environment go to the folder that you originally created it in and execute step 8.

### Linux/Mac OS:

#### Python/Pip Install for Mac OS

1. Go-to the python download page and download python 3.6
    1. https://www.python.org/downloads/
2. Run the installation tool. Make sure the "Add python to PATH" box is checked, and under advanced settings, make sure that the pip box is checked.
3. Confirm that the python version by running one of the following commands in a terminal window, which can be opened via spotlight (the output should be `Python 3.x.x`)
    1. `python3 –version`

#### Python/Pip install for Linux

1. Install *python 3.X* and it's corresponding *pip* using your distro’s specific package manager, details on the different package managers and package names per Linux distribution can be found here https://packaging.python.org/guides/installing-using-linux-tools/
    1. Debian/Ubuntu:  `sudo apt-get install python3 python3-pip`
    2. Fedora 21: `sudo yum install python3 python3-wheel`
    3. Fedora 22: `sudo dnf install python3 python3-wheel`
    4. Arch: `sudo pacman -S python python-pip`
2. Confirm that the python version by running one of the following commands in a terminal window (the output should be `Python 3.x.x`)
    1. `python3 --version`

#### Virtualenv + Django Setup (Linux AND Mac OS):

1. Change directories to where you want to be developing your application
2. Create the virtual environment using the following command
    1. `python3 -m virtualenv <env_name>`
3. Activate the virtual environment in your current shell from the directory you created the environment in (after activating `(env)` should appear in front of your terminal prompt)
    1. `source ./<env_name>/bin/activate`
4. Confirm that python and pip are correctly linked
    1. Python
        1. Run `python --version`
        2. Should return `Python 3.6.x`
    2. Pip
        1. Run `pip --version`
        2. Should return `pip 9.0.1 from <path> (python 3.6)`
5. Install Django in the virtual env with the following command
    1. `pip install django`
