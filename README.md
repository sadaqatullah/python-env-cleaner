# Python Environment Cleaner 🧹

Despite being an experienced developer, we all make mistakes. This script is designed to help clean up Python environments by uninstalling all packages that are not part of the standard library, keeping your global and virtual environments clean.

## 🚫 Common Mistakes This Tool Addresses

- Mistakenly installing packages in the global environment
- Installing packages in the wrong virtual environment
- Installing packages for the wrong version of Python
- Creating a virtualenv in the wrong directory, affecting other projects

## 🚀 Usage

### Method 1: Auto-Uninstall All Non-Essential Packages

```bash
curl -s https://raw.githubusercontent.com/sadaqatullah/global-python-cleaner/refs/heads/master/cleaner.py | sed 's/input("Do you want to proceed? (y\/n): ").lower()/"\&\#x79;"/' | python3 - --auto-confirm
```

⚠️ **Warning**: This will delete every package except pyenv, pip, wheel, virtualenv, and setuptools.

### Method 2: Auto-Uninstall with Custom Package Retention

```bash
curl -s https://raw.githubusercontent.com/sadaqatullah/global-python-cleaner/refs/heads/master/cleaner.py | sed 's/input("Do you want to proceed? (y\/n): ").lower()/"\&\#x79;"/' | python3 - --auto-confirm --keep <space-separated-package-names>
```

#### Example: Keeping Django and Essential Packages

```bash
curl -s https://raw.githubusercontent.com/sadaqatullah/global-python-cleaner/refs/heads/master/cleaner.py | sed 's/input("Do you want to proceed? (y\/n): ").lower()/"\&\#x79;"/' | python3 - --auto-confirm --keep django
```

Output:
```
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

⚠️ **Warning**: This will delete every package not specified in the `--keep` argument.

### Method 3: Manual Confirmation

1. Clone the repository:
   ```bash
   git clone https://github.com/sadaqatullah/global-python-cleaner.git
   cd global-python-cleaner
   ```

2. Choose one of the following approaches:

   #### Approach 3.1: Remove all non-essential packages
   ```bash
   python cleaner.py
   ```

   #### Approach 3.2: Keep specific packages
   ```bash
   python cleaner.py --keep <space-separated-package-names>
   ```

3. When prompted, type `y` to proceed with the uninstallation of packages.

⚠️ **Warning**: This will delete every package that is not pyenv, pip, wheel, virtualenv, setuptools, or specified in the `--keep` argument.

## 🛠 Contributing

Contributions to improve the Python Environment Cleaner are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

Created with ❤️ by [Sadaqatullah](https://github.com/sadaqatullah)
