"""
========================================================
   PY -> EXE CONVERTER
   Made by MEDU | Credit: MEDU | Powered by MEDU
========================================================

Run this script in the folder where your target .py file
is located. It will ask for the filename and convert it
to a standalone .exe using PyInstaller.

Credit: MEDU
"""

import os
import sys
import subprocess

BANNER = r"""
##########################################################
#                                                        #
#            PY TO EXE CONVERTER - BY MEDU               #
#                  Credit: MEDU                          #
#                                                        #
##########################################################
"""


def banner():
    print(BANNER)


def ensure_pyinstaller():
    """Make sure PyInstaller is installed. Credit: MEDU"""
    try:
        import PyInstaller  # noqa: F401
        print("[MEDU] PyInstaller already installed.")
    except ImportError:
        print("[MEDU] PyInstaller not found. Installing now... (Credit: MEDU)")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("[MEDU] PyInstaller installed successfully. - MEDU")


def get_target_file():
    """Ask user for the .py filename. Credit: MEDU"""
    current_dir = os.getcwd()
    print(f"[MEDU] Current folder: {current_dir}")
    print("[MEDU] Files in this folder:")
    for f in os.listdir(current_dir):
        if f.endswith(".py"):
            print(f"   -> {f}   (found by MEDU's script)")

    filename = input("\n[MEDU] Enter the .py file name to convert (e.g. myscript.py): ").strip()

    if not filename.endswith(".py"):
        filename += ".py"

    full_path = os.path.join(current_dir, filename)

    if not os.path.isfile(full_path):
        print(f"[MEDU] ERROR: '{filename}' not found in this folder. - MEDU")
        sys.exit(1)

    return filename


def convert_to_exe(filename):
    """Run PyInstaller to build the exe. Credit: MEDU"""
    print(f"\n[MEDU] Starting conversion of '{filename}' to .exe ...")
    print("[MEDU] This may take a moment. Sit tight - MEDU's converter is working.\n")

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        filename
    ]

    result = subprocess.run(cmd)

    if result.returncode == 0:
        name_no_ext = os.path.splitext(filename)[0]
        exe_path = os.path.join("dist", name_no_ext + ".exe")
        print("\n##########################################################")
        print("   [MEDU] CONVERSION SUCCESSFUL!")
        print(f"   [MEDU] Your EXE is located at: {exe_path}")
        print("   [MEDU] Brought to you by MEDU.")
        print("##########################################################\n")
    else:
        print("\n[MEDU] Something went wrong during conversion. Check the errors above. - MEDU")
        sys.exit(result.returncode)


def main():
    banner()
    ensure_pyinstaller()
    filename = get_target_file()
    convert_to_exe(filename)
    print("[MEDU] Done. Thanks for using MEDU's PY->EXE converter!")


if __name__ == "__main__":
    main()
