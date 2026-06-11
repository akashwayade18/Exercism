def response(hey_bob):
    phrase = hey_bob.strip()
    bob_ans = ""
    if not phrase:
        bob_ans = "Fine. Be that way!"
    elif phrase[-1] == '?' and phrase.isupper():
        bob_ans = "Calm down, I know what I'm doing!"
    elif phrase[-1] == '?':
        bob_ans = "Sure."
    elif phrase.isupper():
        bob_ans = "Whoa, chill out!"
    else:
        bob_ans = "Whatever."
    return bob_ans