print(f"The name of my NAME_AND_MAIN file is: {__name__}")

print(__name__ == "__main__")

if __name__ == "__main__":
    print("name_and_main called directly!")
else:
    print("name_and_main has been imported!")