

with open('README.md' , 'a') as f:
    Name = input('Enter your name: ')
    RollNo = input('Enter your roll no: ')
    f.write('\n')
    f.write(f"| `{Name}` | `{RollNo}`|")
