

def lzw_compress(text):
    dicionary = {chr(k) : k for k in range(256)}
    encoded = list()
    s = text[0]
    for c in text[1:]:
        if s+c in dicionary:
            s = s+c
        else:
            print('> %s' %s)
            encoded.append(dicionary[s])
            print('найдено: %s упаковано как %s' % (s,dicionary[s]))
            dicionary[s+c] = max(dicionary.values()) + 1
            print('Новая последовательность %s  идексирована как %s' % (s+c,dicionary[s+c]))
            s = c
    encoded.append(dicionary[s])
    print('найдено: %s упаковано как %s' %(s,dicionary[s]))
    return encoded


def lzw_decompress(encoded):
    reverse_dictionary = {k:chr(k) for k in range(256)}
    current = encoded[0]
    output = reverse_dictionary[current]
    print ('Распаковано %s' %output)
    print('>%s' % output)
    for element in encoded[1:]:
        previous = current
        current = element
        if current in reverse_dictionary:
            s = reverse_dictionary[current]
            print('Распаковано %s' %s)
            output += s
            print('>%s'  % output)
            new_index = max(reverse_dictionary.keys()) + 1
            reverse_dictionary[new_index] = reverse_dictionary[previous] + s[0]
            print('Новая запись словаря %s с индексом %s' % (reverse_dictionary[previous] + s[0],new_index))
        else:
            print('Не найдено:',current,'output:',reverse_dictionary[previous] + reverse_dictionary[previous][0])
            s = reverse_dictionary[previous]  + reverse_dictionary[previous][0]
            print('Новая запись словаря %s с индексом %s' % (s,max(reverse_dictionary.keys()) + 1))
            reverse_dictionary[max(reverse_dictionary.keys()) + 1 ] = s
            print('Распаковано %s' %s)
            output += s
            print('>%' % output)
        return output