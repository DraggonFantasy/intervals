import random

notes = "CDEFGAB"
all_notes = list("CDEFGAB") + [d + '#' for d in "CDEFGAB"] + [b + 'b' for b in "CDEFGAB"]
accidental_increment = lambda note: next((f for f, s in ((2, '##'), (-2, 'bb'), (1, '#'), (-1, 'b'))
                                          if note.endswith(s)), 0)
note_to_number = lambda note: "C.D.EF.G.A.B".find(note[0]) + 1 + accidental_increment(note)
stop_words = ('q', 'e', 'quit', 'exit', 'выход', 'пока', 'надоело', 'хочу любви')


def iter_notes(n='C'):
    i = notes.find(n) + 1
        


def interval_quality_between_notes(x, y):
    x = notes.find(x[0])
    y = notes.find(y[0])
    #print(f'X = {x}, Y = {y}; xx = {xx}, yy = {yy}')
    if y >= x:
        return y - x + 1
    else:
        return 8 - x + y


def interval_between_notes(x, y):
    q = interval_quality_between_notes(x, y)
    semitones = abs(note_to_number(y) - note_to_number(x)) if note_to_number(y) > note_to_number(x) else 12 - note_to_number(x) + note_to_number(y)
    print(f"Quality = {q} ({note_to_number(y)} - {note_to_number(x)});  Semitones between {x} and {y} is {semitones}")
    if (q, semitones) in ((1, 1), (2, 3), (3, 5), (4, 6), (5, 8), (6, 10), (7, 12)):
        return "ув" + str(q)
    elif (q, semitones) in ((2, 0), (3, 2), (4, 4), (5, 6), (6, 7), (7, 9), (8, 11)):
        return "ум" + str(q)

    if semitones in (0, 5, 7, 12):
        return "ч" + str(q)
    elif semitones in (2, 4, 9, 11):
        return "б" + str(q)
    elif semitones in (1, 3, 8, 10):
        return "м" + str(q)
    return "хз" + str(q)

def make_interval(note, interval):
    if interval == 'ч8':
        return note
    for note2 in all_notes:  #list("CDEFGAB") + [d + '#' for d in "CDEFGAB"] + [b + 'b' for b in "CDEFGAB"]:
        if interval_between_notes(note, note2) == interval:
            return note2
    return None


def mode_1():
    ival = ""
    while ival.lower() not in stop_words:
        note_1 = random.choice(all_notes)
        note_2 = random.choice(all_notes)
        ival = input(f"Какой интервал между {note_1} и {note_2}?  ")
        real_ival = interval_between_notes(note_1, note_2)
        if ival == real_ival:
            print("Верно!")
        else:
            print(f"Неправильно! Ответ - {real_ival}")


def mode_2():
    note_2 = ""
    while note_2.lower() not in stop_words:
        note_1 = random.choice(all_notes)
        ival   = random.choice(intervals)
        note_2 = input(f"Построить {ival} от ноты {note_1}  ")
        real_note_2 = make_interval(note_1, ival)
        if note_2 == real_note_2:
            print("Верно!")
        else:
            print(f"Неправильно! Ответ - {real_note_2}")


print("Привет!\n"
      "Программа умеет работать в двух режимах: \n"
      "  1. Даны две ноты - нужно сказать интервал между ними \n"
      "  2. Дана нота и интервал - нужно сказать вторую ноту.")
mode = None
while mode is None:
    mode = input("В каком режиме работаем? ")

    if mode.startswith('1'):
        mode_1()
    elif mode.startswith('2'):
        mode_2()
    else:
        mode = None

