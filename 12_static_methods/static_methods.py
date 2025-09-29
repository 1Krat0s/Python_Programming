class PathUtils:
    @staticmethod
    def get_extension(filename):
        """Return a file extension (including the dot)"""
        return filename[filename.rfind("."):] if "." in filename else ""
    
    # TODO
    @staticmethod
    # Return the directory path without the file name
    def get_directory(path):
        return path[:path.rfind("/") + 1] if "/" in path else ""
    # Return the file name without the directory path
    def get_basename(path):
        return path[path.rfind("/") + 1:] if "/" in path else ""

# Use the class
print(PathUtils.get_extension("image.img"))
print(PathUtils.get_extension("1.txt"))
print(PathUtils.get_extension("test"))

# TODO
print(PathUtils.get_directory("/workspaces/Python_Programming/12_static_methods"))
print(PathUtils.get_directory("test"))

print(PathUtils.get_basename("/workspaces/Python_Programming/12_static_methods"))
print(PathUtils.get_basename("test"))