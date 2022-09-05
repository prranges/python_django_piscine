#!/usr/local/bin/python3

from local_lib.path import Path


def main():
    path = Path('./files')
    path.mkdir() if not path.exists() else None
    file_example = Path.touch(path / 'text.txt')
    file_example.write_text('\nTest\n', append=False)
    file_example.write_lines(["_" * 20, "Text:", "Some awesome text", "_" * 20], append=False)

    for line in file_example.lines():
        print(line.strip())


if __name__ == '__main__':
    main()
