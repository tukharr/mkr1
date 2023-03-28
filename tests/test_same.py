from main import same


def test_same_lines(prepare_tmp_txt1, prepare_tmp_txt2):
    expected = ["this\n",
                "is\n",
                "file\n",
                ]
    result = same(prepare_tmp_txt1, prepare_tmp_txt2)
    assert expected == result
