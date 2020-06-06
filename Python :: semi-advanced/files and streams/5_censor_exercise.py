def censor(text, blacklist=()):
    output = ''
    for word in text.split(' '):
        if word in blacklist:
            output += '***** '
        else:
            output += word + ' '
    return output.strip()


if __name__ == '__main__':
    with open('censored_words.txt') as file:
        censored_words = file.read().split()
    text = "kurde coś mi nie wyszło, znowu kurka nie działa - mam tego dosyć - do kroćset !"
    print(censor(text, blacklist=censored_words))
