"""
- http://asofttech.github.io/Gbd.IO.Serial/
- Gwilherm Poullennec

https://www.mkdocs.org/
https://www.mkdocs.org/user-guide/configuration/
"""
import os
import platform
import sys
import subprocess
import pathlib

#cd D:\\Users\\poullennecgwi\\Portable\\WPy64-3720\\python-3.7.2.amd64\\Scripts\\mkdocs.exe
#D:\Users\poullennecgwi\Portable\WPy64-3720\python-3.7.2.amd64\python.exe D:\\Users\\poullennecgwi\\Portable\\WPy64-3720\\python-3.7.2.amd64\\Lib\\site-packages\\mkdocs build --clean


# MkDocs Build Script
class MkDocsBuild(object):
    """
    Classe pour générer une documentation avec MkDocs
    """
    def __init__(self):
        """
        Initialisation des répertoires
        """
        self.BUILDDIR = "site"
        self.MKDOCSDIR = "./"
        # Win ou Unix
        if platform.system() == "Windows":
            self.PATH_TO_PYTHON_DIR = pathlib.Path("D:\\Users\\poullennecgwi\\Portable\\WPy64-3720\\python-3.7.2.amd64")
            self.PATH_TO_SITE_PACKAGES = pathlib.Path(self.PATH_TO_PYTHON_DIR / 'Lib' / 'Site-Packages')
            self.PATH_TO_PYTHON_EXE = pathlib.Path(self.PATH_TO_PYTHON_DIR/'python.exe')
            self.PATH_TO_MKDOCS = pathlib.Path(self.PATH_TO_SITE_PACKAGES/'mkdocs')
        elif platform.system() == "Linux":
            self.PATH_TO_PYTHON_DIR = pathlib.Path("/usr/bin")
            self.PATH_TO_SITE_PACKAGES = pathlib.Path('/usr/local/lib/python3.7/dist-packages')
            self.PATH_TO_PYTHON_EXE = pathlib.Path(self.PATH_TO_PYTHON_DIR/'python3')
            self.PATH_TO_MKDOCS = pathlib.Path(self.PATH_TO_SITE_PACKAGES/'mkdocs')

    def run_cmd(self, cmdarray, workingdir):
        """
        :param cmdarray:
        :param workingdir:
        :return:
        """
        proc = subprocess.Popen(cmdarray, cwd=workingdir, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                universal_newlines=True)
        proc_out, proc_err = proc.communicate()
        print(proc_out)
        print(proc_err)
        if proc.returncode != 0:
            raise RuntimeError("Failure to run command")
        return

    def emptydir(self, top):
        """
        Nettoyage du répertoire
        :param top:
        :return:
        """
        if top == '/' or top == "\\":
            return
        else:
            for root, dirs, files in os.walk(top, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))

    def usage(self):
        """
        Affichage de help
        :return:
        """
        print("Please use build.py <target> where <target> is one of")
        print("  build         to make standalone HTML files")
        print("  clean         to clean the output directory:" + self.BUILDDIR)
        print("  publish       publish the site to the gh-pages branch")
        print("  serve         Serve the site out on a port for demoing")

    def build(self):
        """
        Build site
        :return:
        """
        self.clean()
        print("Building MkDocs Files")
        if platform.system() == "Windows":
            cmdopts = ["{}".format(self.PATH_TO_PYTHON_EXE), "{}".format(self.PATH_TO_MKDOCS), "build", "--clean"]
        elif platform.system() == 'Linux':
            cmdopts = ["{}".format(self.PATH_TO_MKDOCS), "build", "--clean"]
        print(cmdopts)
        self.run_cmd(cmdopts, self.MKDOCSDIR)
        print("Build finished. The HTML pages are in " + self.BUILDDIR)

    def publish(self):
        """
        Publish site
        :return:
        """
        self.build()
        print("Publishing MkDocs Files")
        cmdopts = ["{}".format(self.PATH_TO_PYTHON_EXE), "{}".format(self.PATH_TO_MKDOCS), "gh-deploy"]
        self.run_cmd(cmdopts, self.MKDOCSDIR)
        print("Publish finished.")

    def serve(self):
        """
        Run local serveur
        :return:
        """
        print("Starting MkDocs Server http://127.0.0.1:8000")
        cmdopts = ["{}".format(self.PATH_TO_PYTHON_EXE), "{}".format(self.PATH_TO_MKDOCS), "serve"]
        self.run_cmd(cmdopts, self.MKDOCSDIR)
        print("Server Closed.")

    # Clean the Build directory
    def clean(self):
        self.emptydir("site")
        print("Clean finished")

    def main(self):
        if len(sys.argv) != 2:
            self.usage()
            return
        if sys.argv[1] == "build":
            self.build()
        if sys.argv[1] == "clean":
            self.clean()
        if sys.argv[1] == "publish":
            self.publish()
        if sys.argv[1] == "serve":
            self.serve()


if __name__ == "__main__":
    MkDocsBuild().build()
    #MkDocsBuild().serve()