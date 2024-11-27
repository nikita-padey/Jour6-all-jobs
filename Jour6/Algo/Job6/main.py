#Job6

def arrondie(notes):
    notes_arrondies = []

    for i in notes:
        if i < 40:
            print(f"Tu as raté le test avec la note de {i}. Force à toi :)\n")
            continue
        else:
            prochain_multiple = (i + 4) // 5 * 5

            if prochain_multiple - i < 3:
                notes_arrondies.append(prochain_multiple)
            else:
                notes_arrondies.append(i)

    return notes_arrondies


notes = [38, 42, 56, 67, 73, 82, 84, 29, 97]
notes_finales = arrondie(notes)

print("Notes originales :", notes, "\n")
print("Notes arrondies :", notes_finales, "\n")
