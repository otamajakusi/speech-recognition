import speech_recognition as sr

TIMEOUT = 3


def speech2text(lang, apikey):
    r = sr.Recognizer()
    with sr.Microphone() as src:
        r.adjust_for_ambient_noise(src)

        print(f"speak up for {TIMEOUT} seconds")
        audio = r.listen(src, timeout=TIMEOUT)
        print("finished")

    try:
        text = r.recognize_google(audio, language=lang, key=apikey)
        print(f"you said: {text}")
    except Exception as e:
        print(e)


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--lang",
        default="en-US",
        help="select language. default 'en-US'. 'ja-JP' can be used.",
    )
    parser.add_argument(
        "--apikey",
        default=None,
        help="""Google Speech API key. If not specified default key is used.
        To obtain you own API key, follow the instruction below:
        http://www.chromium.org/developers/how-tos/api-keys""",
    )
    args = parser.parse_args()

    speech2text(args.lang, args.apikey)


main()
