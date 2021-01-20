import os


def ingest_text_files():
    root_path = os.path.dirname(os.path.dirname(__file__))
    ingest_files_dir = os.path.join(root_path, "ingest_files")

    txt_files = [os.path.join(ingest_files_dir, filename) for filename in os.listdir(ingest_files_dir)
                 if filename.endswith(".txt")]

    for filepath in txt_files:
        txt_file = open(filepath)
        ingest_str = txt_file.read()
        txt_file.close()

        print(ingest_str)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ingest_text_files()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
