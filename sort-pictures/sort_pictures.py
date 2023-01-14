import pathlib
import shutil


class SortPictures:

    def __init__(self, d_init:str, d_end=""):
        self.d_init_str = d_init  # initial directory
        self.init_dir = pathlib.Path(self.d_init_str)

        self.sorted_dir_str = f"{str(self.init_dir.name)}/sorted"

        self.dirs = {
            "PDF": ["pdf"],
            "Pictures": ["jpg, png"],
            "Videos": ["mp4"],
            "Documents": [""]
        }

        self.dirs_paths = {}  # key - folder name; value - folder path

        try:
            self.__verify()

        except Exception as ex:
            print("Wrong Path")
            exit(1)



    def moveFiles(self):
        """Move all files to the respective dir

        :return:
        """

        # get filenames
        for dir, ext_list in self.dirs.items():
            for ext in ext_list:
                names = sorted(self.init_dir.rglob(f"*.{ext}"))  # returns a list with names sorted
                # move to respective directory
                for filename in names:
                    shutil.copy2(filename, self.dirs_paths[dir])
                    print(f"{filename}\t->\t{self.dirs_paths[dir]}")



        


    def createDirectories(self):
        """Create all directories needed

        The script needs to create all directories for
        each type of file declared in self.dirs.
        """

        for key in self.dirs.keys():  # iterate all keys or directories names
            # declare absolute path with the name of the key, eg. /home/user1/PDF
            path = f"{self.sorted_dir_str}/{key}"
            p_dir = self.__createDirectory(path)

            # the next lines can be deleted
            if (p_dir.exists()):  # verify if exists
                print(f"Directory {key} already exists")

            else:
                
                print(f"Directory {key} has been created")

            self.dirs_paths[key] = str(path)


    def __createDirectory(self, path:str):
        """Create only one directory"""
        dir = pathlib.Path(path)
        dir.mkdir(parents=True, exist_ok=True)
        return dir
        


        

    def showFiles(self):
        """Show all files recursively"""
        for f in self.init_dir.iterdir():
            print(f)


    def __verify(self):
        """Verify if the directory typed exists"""

        if not (self.init_dir.exists()) or not (self.init_dir.is_dir()):
            raise FileNotFoundError

        print(f"{self.init_dir.absolute()} exists")




if "__main__" == __name__:
    dir = "test"
    test = SortPictures(f"./{dir}")
    test.createDirectories()
    test.moveFiles()


