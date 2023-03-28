from main import diff


def test_diff_lines(prepare_tmp_txt1, prepare_tmp_txt2):
    expected = ["not\n",
                "3\n",
                "1\n",
                ]
    result = diff(prepare_tmp_txt1, prepare_tmp_txt2)
    assert expected == result
