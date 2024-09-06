def line_count(file):
    with open('file.txt') as f:
        lines = len(f.readlines())
        print('total number of lines:', lines)
    file.close()