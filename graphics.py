#Maybe graphics, like the acual uno cards
reset1='\033[0m'
def reset():
  print(reset1,end="")
def underline(yuikjh):
  return "\u0332".join(yuikjh)
bold='\033[01m'
zero='''
┌─────────┐
| ┌─────┐ |
| |     | |
| |     | |
| |     | |
| └─────┘ |
└─────────┘'''
one='''
┌─────────┐
|   /|    |
|  / |    |
|    |    |
|    |    |
|  -----  |
└─────────┘'''
two='''
┌─────────┐
|  -──┐   |
|     |   |
|  ┌──┘   |
|  |      |
|  └──-   |
└─────────┘'''
three='''
┌─────────┐
|   ───┐  |
|      |  |
|    ──|  |
|      |  |
|   ───┘  |
└─────────┘'''
four='''
┌─────────┐
| |    |  |
| |    |  |
| └────|  |
|      |  |
|      |  |
└─────────┘'''

five='''
┌─────────┐
|  ┌────  |
|  |      |
|  └───┐  |
|      |  |
|  ────┘  |
└─────────┘'''
six='''
┌─────────┐
|  ┌──    |
|  |      |
|  |───┐  |
|  |   |  |
|  └───┘  |
└─────────┘'''
seven='''
┌─────────┐
|  ────── |
|      /  |
|     /   |
|    /    |  
|   /     |
└─────────┘'''

eight='''
┌─────────┐
|  ┌───┐  |
|  |   |  |
|  |───|  |
|  |   |  |
|  └───┘  |
└─────────┘'''
nine='''
┌─────────┐
|  ┌───┐  |
|  |   |  |
|  └───|  |
|      |  |
|      |  |
└─────────┘'''
plus2='''
┌─────────┐
|    -──┐ |
| |     | |
|─┼─ ┌──┘ |
| |  |    |
|    └──- |
└─────────┘'''
plus4='\033[40m'+'''
┌─────────┐
|   |   | |
| | |   | |
|─┼─└───| |
| |     | |
|       | |
└─────────┘'''+reset1
wild=bold+'\033[40m'+'''
┌─────────┐
|'''+'\033[41m'+'''    '''+'\033[40m'+'''|'''+'\033[44m'+'''    '''+'\033[40m'+'''|\n|'''+'\033[41m'+'''    '''+'\033[40m'+'''|'''+'\033[44m'+'''    '''+'\033[40m'+'''|'''+'''
|────┼────|
'''+'''|'''+'\033[43m'+'''    '''+'\033[40m'+'''|'''+'\033[42m'+'''    '''+'\033[40m'+'''|\n'''+'''|'''+'\033[43m'+'''    '''+'\033[40m'+'''|'''+'\033[42m'+'''    '''+'\033[40m'+'''|'''+'\033[40m'+'''
└─────────┘
'''+bold
skip='''
┌─────────┐
| ┌────/┐ |
| |   / | |
| |  /  | |
| | /   | |
| └/────┘ |
└─────────┘'''
reverse='''
┌─────────┐
|    _    |
|┌──┘ \   |
|| ┌─_/ _ |
|| └───┘ ||
|└───────┘|
└─────────┘
'''
'''
┌─────────┐
|         |
|         |
|         |
|         |
|         |
└─────────┘
'''