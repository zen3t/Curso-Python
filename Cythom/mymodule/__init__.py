try:
    from .uiev import *
except Exception as e:
    import Cython, setuptools, platform, os, sys
    from time import sleep as timesleep

    olddict = os.getcwd()
    dirname = os.path.dirname(__file__)
    os.chdir(dirname)
    files2compile = [
        "uiev_compile.py",
    ]
    for file2compile in files2compile:
        compile_file = os.path.join(dirname, file2compile)
        os.system(" ".join([sys.executable, compile_file, "build_ext", "--inplace"]))
        timesleep(1)
    os.chdir(olddict)
    from .uiev import *
