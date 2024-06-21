# SET OF BOOKS

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


# CHECK FOR DUPLICATES ?
def duplicates_correction(book_to_check):
    for i in Books:
        if book_to_check == i:
            print("Please don't enter duplicates")
            break
      
      
    



#DISPLAY - function that displays all the things in the given list 
def display():
    for i in Books:
        
        print(str(Books.index(i))+ " " + str(i) + "\n")
        
    
        
      
        

#ADD -function that adds a book evertime it is called
#String slicing and fomrating:

def add_book():
    while 1>0:
        print("Enter the infomation in the following information" + "\n")
        
        name_book = input("Name of the book " + "\n")
        autor_book = input ("Name of the autor " + "\n")
        year_book = int(input("Year of the book " + "\n"))
        duplicates_correction((name_book.capitalize(),autor_book.capitalize(),year_book))
        Books.append((name_book.capitalize(),autor_book.capitalize(),year_book))
        continue_add_book = input("Do you wish to add another book? y/n " + "\n")
        if continue_add_book == "y":
            add_book()
        else:
            break

#REMOVE -function that removes a book at a given index everytime it is call *there can be the option to display all the books again

def remove_book():
    while 1>0:
        display()
        Books.remove(int(input("Enter the index of a book you want to remove from the list" + "\n")))
        
        
        continue_remove_book = input("Do you wish to remove another book? y/n" + "\n")
        if continue_remove_book == "y":
           remove_book()
        else:
            break


#SEARCH -fucntion that will check if a book/books have a given criteria (name,year of publishing, autor)

def search_book():
    while 1>0:
        search_term = input("Enter the term you are searching for" + "\n")
        
        print(Books[Books.index(search_term)])

        continue_search_book = input("Do you wish to search another book? y/n" + "\n")
        if continue_search_book == "y":
           search_book()
        else:
            break

#MENU OF OPTION DISPLAY|ADD|REMOVE|SEARCH|EXIT

while 1>0:
      
      print("Hi there, place pick one of the following action  \n DISPLAY|ADD|REMOVE|SEARCH|EXIT " + "\n")
      action = input()
      if action == "DISPLAY":
        display()
      elif action == "ADD":
        add_book()
      elif action == "REMOVE":
        remove_book()
      elif action == "SEARCH":
        search_book()
      elif action == "EXIT":
        break
   







#STATISTICS -function that gives information about the books in the list

#EXIT -function that will either take you one step back or will finish the whole prorgram
