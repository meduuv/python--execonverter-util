# PY → EXE Converter
### Made by **MEDU**

A simple script that converts any Python (`.py`) file into a standalone Windows `.exe`, using PyInstaller under the hood.

---

## ✨ Features
- Auto-installs PyInstaller if it's not already installed
- Lists all `.py` files in the current folder
- Asks you which file to convert
- Builds a single-file `.exe` (no extra files needed to run it)
- Credit: **MEDU** 🛠️

---

## 📦 Requirements
- Python 3.7+ installed
- Windows (to actually *run* the resulting `.exe`; you can build it on other OSes too, but the `.exe` only runs on Windows)
- Internet connection (only needed the first time, to install PyInstaller)

---

## 🚀 How to Use

1. Put `py2exe_by_medu.py` in the **same folder** as the `.py` file you want to convert.
2. Open a terminal / command prompt in that folder.
3. Run:
   ```
   python py2exe_by_medu.py
   ```
4. The script will:
   - Check/install PyInstaller
   - Show you all `.py` files in the folder
   - Ask you to type the filename you want to convert (e.g. `myscript.py` or just `myscript`)
5. Wait for the build to finish.
6. Your `.exe` will be inside the new `dist/` folder, e.g.:
   ```
   dist/myscript.exe
   ```

---

## 📁 What Gets Created
After running, PyInstaller creates some extra files/folders — this is normal:
- `dist/` → contains your final `.exe` (this is the only one you need)
- `build/` → temporary build files (safe to delete)
- `*.spec` → PyInstaller config file (safe to delete, or keep if you want to rebuild easily)

---

## ❓ Troubleshooting

**"PyInstaller not found" keeps appearing**
Make sure `pip` works properly. Try manually:
```
pip install pyinstaller
```

**The .exe doesn't run / closes instantly**
Run it from a terminal (`cmd`) instead of double-clicking, so you can see any error messages:
```
dist\myscript.exe
```

**Antivirus flags the .exe**
This is a common false positive with PyInstaller-built executables. It's not actually a virus — you may need to whitelist it.

**My script uses extra files (images, data, etc.)**
This script does a simple `--onefile` build. If your project needs extra files bundled in, you'll need a custom PyInstaller `--add-data` setup.

---

## 🙌 Credits
**Script & idea: MEDU**
Built using [PyInstaller](https://pyinstaller.org/).
