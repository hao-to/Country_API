import wikipedia

wikipedia.set_lang("en")
print(wikipedia.summary("Japan", sentences=2, auto_suggest=False))

