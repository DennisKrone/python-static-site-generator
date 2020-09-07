from typing import List
from pathlib import Path
import shutil


class Parser:

    extensions = List[str]

    def valid_extension(self, extension):
        if extension in Parser.extensions:
            return True
        else:
            return False

    def parse(path, source, dest):
        raise NotImplementedError

    def read(path):
        with open(path) as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest + "/" + path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)

    def copy(path, source, dest):
        shutil.copy2(path, dest + "/" + source + "/" + path)
