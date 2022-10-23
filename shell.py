import kepler

while True:
    text = input('kepler > ')
    result, error = kepler.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)