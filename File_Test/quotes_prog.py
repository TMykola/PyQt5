with open("quotes.txt", "r", encoding= "utf-8") as file:
    print(file.read())
with open("quotes.txt", "a", encoding= "utf-8") as file:
    file.write(input())
    file.write("(Т.Г Шевченко)")



