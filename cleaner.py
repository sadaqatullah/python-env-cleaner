import subprocess
import sys

# Essential packages that should remain in the global environment
ESSENTIAL_PACKAGES = {
    "pip",
    "setuptools",
    "wheel",
    "virtualenv",
    "pyenv",  # Since you mentioned using pyenv
}

def get_installed_packages():
    result = subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True)
    return [line.split('==')[0] for line in result.stdout.split('\n') if line]

def uninstall_packages(packages):
    for package in packages:
        print(f"Uninstalling {package}...")
        subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", package])

def main():
    installed_packages = set(get_installed_packages())
    packages_to_remove = installed_packages - ESSENTIAL_PACKAGES

    print("The following packages will be uninstalled:")
    for package in packages_to_remove:
        print(f"  - {package}")

    confirmation = input("Do you want to proceed? (y/n): ").lower()
    if confirmation == 'y':
        uninstall_packages(packages_to_remove)
        print("Cleanup completed.")
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()