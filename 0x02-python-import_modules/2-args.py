#!/usr/bin/python3
argv = sys.argv[1:]

number_of_arguments = len(argv)
print(f"Number of arguments{'s' if number_of_arguments != 1 else ''}:
      {number_of_arguments}{'.' if number_of_arguments == 0 else ':'}")

for x, arg in enumerate(argv, start=1):
    print(f"{x}: {arg}")

    if number_of_arguments == 0:
        print()
