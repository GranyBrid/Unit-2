favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}

for name in favorite_languages.keys():
    print(name.title())
print()
for name in favorite_languages.keys():
    print(name.title())
print()
for languages in favorite_languages.values():
    print(languages.title())
print()
for name,language in favorite_languages.items():
    print(f"{name.title()}'s favorite programming language is {language.title()}")