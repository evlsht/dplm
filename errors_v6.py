# pronoun2file
# aarticle2file
# the2file
# devided lines???
# attributes?

import re
import codecs

def pronoun(file):
    result = []
    exceptions = [u'also', u'once', u'fell']
    with open(file, encoding='utf-8') as f:
        text = f.read()
        pattern = re.compile(
                u'(^|[^\w])([Hh]e|[Ss]he|[Ii]t) ([a-z\']+[a-ce-rt-z])([^\w]|$)')
                #last leters not d
        for m in re.finditer(pattern, text):
            word = m.group(3)
            if word[-3:] != u"n't" and word not in exceptions:
                line = str(m.start(3)) + u' ' + str(m.end(3)) + u'\t' + word
                result.append(line)
    return result


def aarticle(file):
    result = []
    with open (file, encoding='utf-8') as f:
        text = f.read()
        pattern = re.compile(u'(^|[^\w])([Aa]) ([eyuioa][a-z]+)([^\w]|$)')
        for m in re.finditer(pattern, text):
            line = str(m.start(2)) + u' ' + str(m.end(2)) + u'\t' + m.group(2)
            result.append(line)
    return result

def thecountries(file):
    result = []
    s = [u'UK',u'Netherlands', u'USA', u'Bahamas', u'Gambia', u'Philippines']
    with open (file, encoding='utf-8') as f:
        text = f.read()
        for country in s:
            pattern = re.compile(u'(^|[^\w])([Aa]n? |(?<![Tt]he ))' + country +\
                                 u'([^\w]|$)')
            for m in re.finditer(pattern, text):
                line = str(m.start(2)) + u' ' + str(m.end(2)) + u'\t' +\
                       m.group(2)
#                print (m.groups())
                result.append(line)
    return result


def theadj(file):
    result = []
    with open (file, encoding='utf-8') as f:
        text = f.read()
        pattern = re.compile(u'(^|[^\w])([Aa]n? |(?<![Tt]he ))([A-Za-z]+est)([^\w]|$)')
        for m in re.finditer(pattern, text):
            line = str(m.start(2)) + u' ' + str(m.end(2)) + u'\t' + m.group(2)
            result.append(line)
    return result

def pronoun2file(file, i=0, mode='a'):         
    arr = pronoun(file)
    file_out = re.sub(u'txt', u'ann', file)
    with open(file_out, mode, encoding='utf-8') as fw:
        for a in arr:
            i += 1
            word = a.partition(u'\t')[2]
            word = re.sub(u'(\w+o)([^\w]|$)', u'\g<1>es', word)
            word = re.sub(u'(\w+[^eyuioa])y([^\w]|$)', u'\g<1>ies', word)
            word = re.sub(u'(\w+[^s])([^\w]|$)', u'\g<1>s', word)
            line = u'T' + str(i) + u'\t' + u'Person' + u' ' + a + u'\n' +\
                    u'#' + str(i) + u'\t' + u'AnnotatorNotes T' + str(i) +\
                    u'\t' + word + u'\n'
            fw.write(line)
            print (line)
    print (u'Annotation file: ' + file_out)
    return i


def aarticle2file(file, i=0, mode='a'):
    arr = aarticle(file)
    file_out = re.sub(u'txt', u'ann', file)
    with open(file_out, mode, encoding='utf-8') as fw:
        for a in arr:
            i += 1
            word = a.partition(u'\t')[2] + u'n'
            line = u'T' + str(i) + u'\t' + u'Art_choice' + u' ' + a + u'\n' +\
                    u'#' + str(i) + u'\t' + u'AnnotatorNotes T' + str(i) +\
                    u'\t' + word + u'\n'
            fw.write(line)
            print (line)
    print (u'Annotation file: ' + file_out)
    return i


def the2file(file, i=0, mode='a'):
    arr = thecountries(file) + theadj(file)
    file_out = re.sub(u'txt', u'ann', file)
    with open(file_out, mode, encoding='utf-8') as fw:
        for a in arr:
            i += 1
            word = a.partition(u'\t')[2]
            line = u'T' + str(i) + u'\t' + u'Art_choice' + u' ' + a + u'\n'
            if word == u'':
                line = line + u'A' + str(i) + u'\tAdd\t' + u'T' + str(i) + u'\n'
            line = line + u'#' + str(i) + u'\t' + u'AnnotatorNotes T' +\
                   str(i) + u'\t' + u'the ' + u'\n'
            print (line)
            fw.write(line)
    print (u'Annotation file: ' + file_out)
    return i


#arr = pronoun(u'test.txt')
#arr = aarticle(u'test.txt')
#arr = thecountries(u'test.txt')
#arr = theadj(u'test.txt')
#for s in arr:
#    print (s)


file_in = u'test.txt'
#file_in = u'esl_0011.txt'
i = pronoun2file(file_in, i=0, mode='w')
i = aarticle2file(file_in, i)
i = the2file(file_in, i)
                
    
