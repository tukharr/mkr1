import pytest
import os


@pytest.fixture(autouse=True)
def prepare_tmp_txt1(tmp_path):
    target_file1 = os.path.join(tmp_path, "file1.txt")
    with open(target_file1, 'w') as file:
        lines = ["this\n"
                 "is\n"
                 "file\n"
                 "1\n"
                 ]
        file.writelines(lines)
    return target_file1


@pytest.fixture(autouse=True)
def prepare_tmp_txt2(tmp_path):
    target_file2 = os.path.join(tmp_path, "file2.txt")
    with open(target_file2, 'w') as file:
        lines = ["this\n"
                 "is\n"
                 "not\n"
                 "file\n"
                 "3\n"
                 ]
        file.writelines(lines)

    return target_file2
