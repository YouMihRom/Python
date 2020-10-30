user_list = [1, 2.6, 'some text', True, None, b'some bytes',
             (1, 45, 678, None),
             [43, 56, 23, 'four'],
             {'key': 'value', 'number': 'text'},
             {'new text', 'next text'}
             ]
for items in user_list:
    print(f'{str(items):>30}: type={type(items)}')
