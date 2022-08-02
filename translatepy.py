def tpy(text, dess):
    from googletrans import Translator

    translator = Translator()
    r = translator.translate(text, dest=dess)

    t1 = r.text
    t2 = r.pronunciation
    return [t1, t2]


def trlist():
    import googletrans
    for p in googletrans.LANGUAGES:
        print(f"{p}: {googletrans.LANGUAGES[p]}")
