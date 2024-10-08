# python-env-cleaner
Despite being an experienced developer, I still make 
mistakes. 

Here is the list of mistakes I make:
* Mistakenly installing packages in the global environment
* Mistakenly installing packages in the wrong virtual environment
* Mistakenly installing packages in the wrong version of Python
* Mistakenly creating a virtualenv in the wrong directory affecting other projects.

This script is designed to help me clean up the 
environment by uninstalling all packages that are not 
part of the standard library. And thus keeping my global
and virtual env clean.

## Usage

### Method 1 
For Auto Proceeding to Uninstall Every Package
```bash 
curl -s https://raw.githubusercontent.com/sadaqatullah/global-python-cleaner/refs/heads/master/cleaner.py | sed 's/input("Do you want to proceed? (y\/n): ").lower()/"\&\#x79;"/' | python3 - --auto-confirm
```
#### Warning
This will delete every package that is not  pyenv, pip, wheel, virtualenv, setuptools

### Method 2
For Auto Proceeding to Uninstall Packages but keeping certain packages in the env
```bash
curl -s https://raw.githubusercontent.com/sadaqatullah/global-python-cleaner/refs/heads/master/cleaner.py | sed 's/input("Do you want to proceed? (y\/n): ").lower()/"\&\#x79;"/' | python3 - --auto-confirm --keep <space-separated-package-names>
```
#### Example:
You want to keep django and essential packages. Modify the command as follows:
```bash
curl -s https://raw.githubusercontent.com/sadaqatullah/global-python-cleaner/refs/heads/master/cleaner.py | sed 's/input("Do you want to proceed? (y\/n): ").lower()/"\&\#x79;"/' | python3 - --auto-confirm --keep django
```
```bash
The following packages will be kept:
  - setuptools
  - django
  - pyenv
  - wheel
  - pip
  - virtualenv
The following packages will be uninstalled:
    - package-1
    - package-2
    ...
    - package-n
Cleanup completed.
```

#### Warning
This will delete every package that is not provided at the end of the command

### Method 3
For Manual Proceeding to Uninstall Packages

1. Clone the Repo
#### Approach 3.1
2. Run the following command remove every package that is not  pyenv, pip, wheel, virtualenv, setuptools
```bash
python cleaner.py
```
3. When prompted, type `y` to proceed with the uninstallation of packages.

#### Approach 3.2
2. Run the following command remove every package but keep the packages you want
```bash
python cleaner.py --keep <space-separated-package-names>
```
3. When prompted, type `y` to proceed with the uninstallation of packages.

#### Warning
This will delete every package that is not  pyenv, pip, wheel, virtualenv, setuptools
