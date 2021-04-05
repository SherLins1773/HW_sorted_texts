def line_counter(doc):
    with open(doc, encoding='utf-8') as f:
        x = -1
        while True:
            x += 1
            line = f.readline()
            if not line:
                break
    f.close()
    return x


def rewriter(doc):
    with open(doc, encoding='utf-8') as f:
        lines = f.readlines()
    f.close()
    return lines


numb_list = [line_counter('1.txt'), line_counter('2.txt'), line_counter('3.txt')]

with open('finish.txt', 'w', encoding='utf-8') as f:
    if line_counter('1.txt') == sorted(numb_list)[0]:
        f.write('1.txt \n')
        f.write(str(line_counter('1.txt')) + '\n')
        f.write(str(rewriter('1.txt')) + '\n')
    elif line_counter('2.txt') == sorted(numb_list)[0]:
        f.write('2.txt \n')
        f.write(str(line_counter('2.txt')) + '\n')
        f.write(str(rewriter('2.txt')) + '\n')
    else:
        f.write('3.txt \n')
        f.write(str(line_counter('3.txt')) + '\n')
        f.write(str(rewriter('3.txt')) + '\n')
    if line_counter('1.txt') == sorted(numb_list)[1]:
        f.write('1.txt \n')
        f.write(str(line_counter('1.txt')) + '\n')
        f.write(str(rewriter('1.txt')) + '\n')
    elif line_counter('2.txt') == sorted(numb_list)[1]:
        f.write('2.txt \n')
        f.write(str(line_counter('2.txt')) + '\n')
        f.write(str(rewriter('2.txt')) + '\n')
    else:
        f.write('3.txt \n')
        f.write(str(line_counter('3.txt')) + '\n')
        f.write(str(rewriter('3.txt')) + '\n')
    if line_counter('1.txt') == sorted(numb_list)[2]:
        f.write('1.txt \n')
        f.write(str(line_counter('1.txt')) + '\n')
        f.write(str(rewriter('1.txt')))
    elif line_counter('2.txt') == sorted(numb_list)[2]:
        f.write('2.txt \n')
        f.write(str(line_counter('2.txt')) + '\n')
        f.write(str(rewriter('2.txt')))
    else:
        f.write('3.txt \n')
        f.write(str(line_counter('3.txt')) + '\n')
        f.write(str(rewriter('3.txt')))
    f.close()
