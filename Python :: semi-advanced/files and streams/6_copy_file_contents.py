def copy_file_content(source_filename: str, target_filename: str):
    with open(source_filename) as source:
        with open(target_filename, 'a') as target:
            for line in source:
                target.write(line)


if __name__ == '__main__':
    copy_file_content('python_zen.txt', 'coptied_python_zen.txt')
