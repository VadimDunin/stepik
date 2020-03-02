example = False

if example:
    s = 'My Name is Julia'

    if 'Name' in s:
        print('Substring found')

    index = s.find('Name')
    if index != -1:
        print(f'Substring found at index {index}')


def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, "expected '{}' to be substring of '{}'".format(substring, full_string)


full_strings = ["fulltext", '1', "some_text"]
substrings = ["some_value", "1", "some" ]


i = 0
while i < len(full_strings):
    test_substring(full_string=full_strings[i], substring=substrings[i])