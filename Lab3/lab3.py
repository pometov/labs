def text_handler(list):
    text = list.split('.')
    x = len(text)
    i = 0
    new_text =''
    while(i < x):
        new_text += collect(pars(text[i]))
        i+=1
    return new_text

def pars(list):
    i=0
    str = list.split()
    n = len(str)
    while (i < n):
        buf = str[i]
        j = i+1
        while (j < n):
            if (buf.lower() == str[j].lower()):
                l = j + 1
                while (l < n):
                    str [l-1] = str [l]
                    l+=1
                str.remove(str[n-1])
                n-=1
            j+=1
        i+=1
    return str

def collect(list):
    i = 0
    string_to_coll =''
    while (i < len(list)):
        string_to_coll += list[i]
        if (i == len(list) - 1 ):
            string_to_coll+='. '
        else: string_to_coll += ' '
        i+=1
    return string_to_coll




s = ''
while True:
    s = input("Введите текст для удаления повторяющихся слов в предложениях:\n")
    print(text_handler(s))





