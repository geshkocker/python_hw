zen_of_python = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
better_c = zen_of_python.count('better')
never_c = zen_of_python.count('never')
is_c = zen_of_python.count('is')

zen_of_python_upper = zen_of_python.upper()

zen_of_python_replace = zen_of_python.replace('i', '&')

print(f'Word "better" is used {better_c} times')
print(f'Word "never" is used {never_c} times')
print(f'Word "is" is used {is_c} times')
print(zen_of_python_upper)
print(zen_of_python_replace)
