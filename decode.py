def replace_all(text, dct):
    trancl_dct = str.maketrans(dct)
    text = text.translate(trancl_dct)
    return text


text = input()
c_dict = {'Ф': 'а', 'И': 'б', 'Й': 'в', 'P': 'г', 'С': 'д', 'г': 'е', 'ф': 'ё', 'J': 'ж', 'ю': 'з', '[': 'и', 'Е': 'й',
          'E': 'к', 'к': 'л', '3': 'м', 'Y': 'н', ';': 'о', '>': 'п', 'ъ': 'р', 'З': 'с', 'В': 'т', '0': 'у', 'Ы': 'ф',
          'Ц': 'х', 'М': 'ц', '(': 'ч', 'щ': 'ш', 'Ю': 'щ', '&': 'ъ', 'L': 'ы', '@': 'ь', '/': 'э', 'd': 'ю',
          '7': 'я', '-': '1', 'Ё': '2', 'V': '3', 'Ч': '4', 's': '5', ' ': '6', 'э': '7', '2': '8', '+': '9', 'z': '0',
          '|': '?', '¡': '!', '%': '.', '*': ',', '^': '+', '¿': '-', 'C': ' '}
text = replace_all(text, c_dict)
print(text)
