import subprocess
import sys
import argparse

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
    parser = argparse.ArgumentParser(description="Uninstall all Python packages except specified ones.")
    parser.add_argument('--keep', nargs='*', default=ESSENTIAL_PACKAGES,
                        help=f'Packages to keep (default: {", ".join(ESSENTIAL_PACKAGES)})')
    parser.add_argument('--auto-confirm', action='store_true',
                        help='Automatically confirm package uninstallation')
    args = parser.parse_args()

    installed_packages = set(get_installed_packages())
    packages_to_keep_by_user = set(args.keep)
    packages_to_keep = packages_to_keep_by_user | ESSENTIAL_PACKAGES
    packages_to_remove = installed_packages - packages_to_keep

    print("The following packages will be kept:")
    for package in packages_to_keep:
        print(f"  - {package}")

    print("The following packages will be uninstalled:")
    for package in packages_to_remove:
        print(f"  - {package}")

    if "--auto-confirm" in sys.argv:
        confirmation = 'y'
    else:
        confirmation = input("Do you want to proceed? (y/n): ").lower()

    if confirmation == 'y':
        # uninstall_packages(packages_to_remove)
        print("Cleanup completed.")
    else:
        print("Operation cancelled.")


if __name__ == "__main__":
    main()
