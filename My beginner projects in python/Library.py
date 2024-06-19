print("Hi there, I am your librarÿ's managment system")
action = input("Please choose one of the following actions: \n display|add|remove|search|exit")

#list of books
Books = [
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("1984", "George Orwell", 1949),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
    ("The Catcher in the Rye", "J.D. Salinger", 1951),
    ("The Lord of the Rings", "J.R.R. Tolkien", 1954),
    ("Pride and Prejudice", "Jane Austen", 1813),
    ("The Hobbit", "J.R.R. Tolkien", 1937),
    ("Moby Dick", "Herman Melville", 1851),
    ("Jane Eyre", "Charlotte Bronte", 1847),
    ("War and Peace", "Leo Tolstoy", 1869)]


def display():
    print("Here are all books")
    for i in Books:
        print(str(i) + " " + Books[i] + "\n")
exit

    
continue_program = True

def add_a_book(name_of_the_book,autor,year_of_relsese):
    back = False
    while back == False:
       print("Please enter the information in the following manner: Name of the book, Autor and year of release")
       Books.append((name_of_the_book,autor,year_of_relsese))
       continue_add = input("Do you wish to continue y/n")
       if continue_add == "n":
        exit
     
def remove_a_book():
    back = False
    while back == False:
       print("Here is list of all books, enter the numbe infornt of the book you want to get rid of")
       index_remove = int(input("Type the number: "))
       Books.remove(index_remove)
       continue_add = input("Do you wish to continue y/n")
       if continue_add == "n":
        exit
     
def search_a_book():
    criteria_search= input("Please choose a criteria for searching the book - name, autor or year of relese")
    if criteria_search.lower() == "name":
       name_of_book = input("What is the name? ")
       for i in Books:
          if Books[i][0].lower() == name_of_book.lower():
             print("Here is what I have found: " + "\n" +  str(Books[i]))
    elif criteria_search.lower() == "year":
       year_of_book = input("What is the year of relelse? ")
       for i in Books:
          if Books[i][1].lower() == year_of_book.lower():
             print("Here is what I have found: " + "\n" +  str(Books[i]))
       
    


    

    while continue_program == True:
        action = input("Please choose one of the following actions: \n display|add|remove|search|exit")
        if action.lower() == "add":
           add_a_book
        elif action.lower() == "remove":
           remove_a_book
        elif action.lower() == "display":
           display()
        
                 
           





