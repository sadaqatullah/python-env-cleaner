# python-env-cleaner
Despite being an experienced developer, I still make 
mistakes. 

Here is the list of mistakes I make:
* Mistakenly installing packages in the global environment
* Mistakenly installing packages in the wrong virtual environment
* Mistakenly installing packages in the wrong version of Python
* Mistakenly creating a virtualenv in the wrong directory affecting other projects.

This script is designed to help me clean up the global 
environment by uninstalling all packages that are not 
part of the standard library. And thus keeping my global
and virtual env clean.

## Usage

### For Auto Proceeding to Uninstall Packages
```bash 
curl -s https://raw.githubusercontent.com/sadaqatullah/global-python-cleaner/refs/heads/master/cleaner.py | sed 's/input("Do you want to proceed? (y\/n): ").lower()/"\&\#x79;"/' | python3 - --auto-confirm
```

### For Manual Proceeding to Uninstall Packages
1. Clone the Repo
2. Run the following command
```bash
python cleaner.py
```
3. When prompted, type `y` to proceed with the uninstallation of packages.

## Warning