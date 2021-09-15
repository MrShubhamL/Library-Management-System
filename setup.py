import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Program Files\Python37\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Program Files\Python37\tcl\tk8.6"

executables = [cx_Freeze.Executable("main.py", base=base, icon="Icon.ico")]


cx_Freeze.setup(
    name = "Library Managment",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["Icon.ico",'database','icons','themes','tcl86t.dll','tk86t.dll','library2.ui','Login2.ui','AboutUs.ui','icons_rc.py','res_rc.py','res2_rc.py','icons.qrc','res.qrc','res2.qrc','xlwt']}},
    version = "8.3",
    description = "Library Management | Developed By SHUBHAM LOHAR",
    executables = executables
    )
