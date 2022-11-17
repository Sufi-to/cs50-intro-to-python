import emoji


emo = input("Input: ")

emoj = emoji.emojize(emo, language='alias')

print(f"Output: {emoj}")
