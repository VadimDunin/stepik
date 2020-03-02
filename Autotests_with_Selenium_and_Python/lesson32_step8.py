def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result, "expected {}, got {}".format(expected_result,actual_result)


expected_results = [8, 11, 11]
actual_results = [11, 11,15]

i = 0
while i < len(expected_results):
    test_input_text(expected_results[i],actual_results[i])
    i += 1
