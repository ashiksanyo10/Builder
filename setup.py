from cx_Freeze import setup, Executable

# Application metadata
app_name = "GTI Duplicate Check"
app_version = "1.0"
app_description = "Checks for GTI duplicates and alerts operators."

# Dependencies
build_options = {
    "packages": ["tkinter", "selenium", "mysql.connector"],
    "include_files": ["../assets/icon.ico"],
}

# Executable settings
executables = [
    Executable(
        script="main.py",
        base="Win32GUI",
        target_name="GTIChecker.exe",
        icon="../assets/icon.ico"
    )
]

# Setup configuration
setup(
    name=app_name,
    version=app_version,
    description=app_description,
    options={"build_exe": build_options},
    executables=executables
)
