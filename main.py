import speech_recognition as sr

TIMEOUT = 3


def speech2text(lang):
    r = sr.Recognizer()
    with sr.Microphone() as src:
        r.adjust_for_ambient_noise(src)

        print(f"speak up for {TIMEOUT} seconds")
        audio = r.listen(src, timeout=TIMEOUT)
        print("end")

    try:
        # text = r.recognize_google(audio, language="ja-JP")
        text = r.recognize_google(audio, language=lang)
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
    args = parser.parse_args()

    speech2text(args.lang)


main()
