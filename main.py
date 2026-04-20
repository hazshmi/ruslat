alphabet = {
    'а': 'a', 'А': 'A', 'б': 'b', 'Б': 'B', 'в': 'v', 'В': 'V',
    'г': 'g', 'Г': 'G', 'д': 'd', 'Д': 'D', 'е': 'e', 'Е': 'E',
    'ё': 'ë', 'Ё': 'Ë', 'ж': 'ž', 'Ж': 'Ž', 'з': 'z', 'З': 'Z',
    'и': 'i', 'И': 'I', 'й': 'j', 'Й': 'J', 'к': 'k', 'К': 'K',
    'л': 'l', 'Л': 'L', 'м': 'm', 'М': 'M', 'н': 'n', 'Н': 'N',
    'о': 'o', 'О': 'O', 'п': 'p', 'П': 'P', 'р': 'r', 'Р': 'R',
    'с': 's', 'С': 'S', 'т': 't', 'Т': 'T', 'у': 'u', 'У': 'U',
    'ф': 'f', 'Ф': 'F', 'х': 'x', 'Х': 'X', 'ц': 'c', 'Ц': 'C',
    'ч': 'č', 'Ч': 'Č', 'ш': 'š', 'Ш': 'Š', 'щ': 'ŝ', 'Щ': 'Ŝ',
    'ъ': '‘', 'Ъ': '‘', 'ы': 'y', 'Ы': 'Y', 'э': 'è', 'Э': 'È',
    'ю': 'ü', 'Ю': 'Ü', 'я': 'ä', 'Я': 'Ä', 'ь': '-', 'Ь': '-'
}

softcon = {
    'бь': 'b́', 'Бь': 'B́', 'бЬ': 'b́', 'БЬ': 'B́',
    'вь': 'v́', 'Вь': 'V́', 'вЬ': 'v́', 'ВЬ': 'V́',
    'гь': 'ǵ', 'Гь': 'Ǵ', 'гЬ': 'ǵ', 'ГЬ': 'Ǵ',
    'дь': 'd́', 'Дь': 'D́', 'дЬ': 'd́', 'ДЬ': 'D́',
    'зь': 'ź', 'Зь': 'Ź', 'зЬ': 'ź', 'ЗЬ': 'Ź',
    'кь': 'ḱ', 'Кь': 'ḱ', 'кЬ': 'ḱ', 'КЬ': 'ḱ',  
    'ль': 'ĺ', 'Ль': 'Ĺ', 'лЬ': 'ĺ', 'Ль': 'Ĺ',  
    'мь': 'ḿ', 'Мь': 'Ḿ', 'мЬ': 'ḿ', 'МЬ': 'Ḿ',
    'нь': 'ń', 'Нь': 'Ń', 'нЬ': 'ń', 'НЬ': 'Ń',
    'пь': 'ṕ', 'Пь': 'Ṕ', 'пЬ': 'ṕ', 'ПЬ': 'Ṕ',
    'рь': 'ŕ', 'Рь': 'Ŕ', 'рЬ': 'ŕ', 'РЬ': 'Ŕ',
    'сь': 'ś', 'Сь': 'Ś', 'сЬ': 'ś', 'СЬ': 'Ś',
    'ть': 't́', 'Ть': 'T́', 'тЬ': 't́', 'ТЬ': 'T́',
    'фь': 'f́', 'Фь': 'F́', 'фЬ': 'f́', 'ФЬ': 'F́',
    'хь': 'h', 'Хь': 'H', 'хЬ': 'h', 'ХЬ': 'H'
}

soft, nosoft = set('бвгдзклмнпрстфхБВГДЗКЛМНПРСТФХ'), set('жйцчшщЖЙЦЧШЩ')

def ruslat(text: str) -> str:
    i, res = 0, []
    while i < len(text):
        if i + 1 < len(text) and text[i+1] == 'ь':
            if text[i] in soft:
                pair = text[i:i+2]
                res.append(softcon.get(pair, alphabet.get(text[i], text[i]) + '-'))
                i += 2
                continue
            elif text[i] in nosoft:
                res.append(alphabet.get(text[i], text[i]))
                i += 2
                continue
        if text[i] == 'ь':
            raise ValueError('мягкий знак как отдельная буква.')
        res.append(alphabet.get(text[i], text[i]))
        i += 1
    return ''.join(res)

def latrus(text: str) -> str:
    i, res = 0, []
    rev_simple = {v: k for k, v in alphabet.items()}
    rev_simple['‘'] = 'ъ'
    rev_soft = {v: k for k, v in softcon.items()}
    n = len(text)

    def get_cyr(seq: str) -> str:
        if seq in rev_soft:
            return rev_soft[seq]
        return rev_simple.get(seq, seq)

    while i < n:
        if i + 1 < n and text[i+1] == '\u0301':
            pair = text[i] + text[i+1]
            if pair in rev_soft:
                res.append(get_cyr(pair))
                i += 2
                continue
        ch = text[i]
        if ch in rev_soft:
            res.append(rev_soft[ch])
            i += 1
            continue
        if ch in rev_simple:
            res.append(rev_simple[ch])
            i += 1
            continue
        res.append(ch)
        i += 1
    return ''.join(res)

if __name__ == "__main__":
    mode = input("Выберите направление: 1 - кириллица -> латиница, 2 - латиница -> кириллица: ")
    text = input("Введите текст: ")
    if mode == '1':
        print(ruslat(text))
    elif mode == '2':
        print(latrus(text))
    else:
        print("Ошибка!")