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
        tar.extractall()


if __name__ == '__main__':
    text = """Ala ma kota,
    kot ma giwerę,
    na górze róże,
    na dole fiołki"""
    save_as_compressed(text, 'archive.gz')
    read_compressed_archive('archive.gz')

    compress_multiple_files(['python_zen.txt', 'userdata.csv', 'accesslog.txt'], 'archive2.tar.gz')
    extract_tar_file('archive2.tar.gz')
