import gzip
import tarfile
from typing import List


def save_as_compressed(content: str, filename: str):
    with gzip.open(filename, 'wt', compresslevel=9) as target:
        target.write(content)


def read_compressed_archive(archivename: str):
    with gzip.open(archivename, 'rt') as file:
        for line in file:
            print(line)


def compress_multiple_files(files: List[str], target: str):
    with tarfile.open(target, 'w') as tar:
        for file in files:
            tar.add(file)


def extract_tar_file(tar_name: str):
    with tarfile.open(tar_name, 'r') as tar:
        
        import os
        
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar)


if __name__ == '__main__':
    text = """Ala ma kota,
    kot ma giwerę,
    na górze róże,
    na dole fiołki"""
    save_as_compressed(text, 'archive.gz')
    read_compressed_archive('archive.gz')

    compress_multiple_files(['python_zen.txt', 'userdata.csv', 'accesslog.txt'], 'archive2.tar.gz')
    extract_tar_file('archive2.tar.gz')
