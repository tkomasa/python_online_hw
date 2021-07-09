text_org = input("Enter string: ")

text_last = text_org[len(text_org)-1]
text_rest = text_org[:len(text_org)-1]
text_shift = text_last + text_rest


print(text_org)
print(text_shift)
