Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> word = "supercalifragilisticexpialidocious"
>>> word[0]
's'
>>> word[2]
'p'
>>> word[5:9:1]
'cali'
>>> word[5::2}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> word[5::2]
'clfaiitcxildcos'
>>> word[::-1]
'suoicodilaipxecitsiligarfilacrepus'
>>> word[word.index("cali"):word.index("frag")]
'cali'
>>> word[word.index("doc"):]
'docious'
>>> word[word.index("fra"):word.index("e")]
''
>>> 