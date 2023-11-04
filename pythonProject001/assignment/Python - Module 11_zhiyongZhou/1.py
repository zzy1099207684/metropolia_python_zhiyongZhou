# Implement the following class hierarchy using Python: A publication can be either a book or a magazine.
# Each publication has a name. Each book also has an author and a page count, whereas each magazine has a chief editor.
# Also write the required initializers to both classes.
# Create a print_information method to both subclasses for printing out all information of the publication in question.
# In the main program, create publications Donald Duck (chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages).
# Print out all information of both publications using the methods you implemented.
class Publication:
    def __init__(self, name):
        self.name = name;


class Book(Publication):
    def __init__(self, name, author, pageCount):
        super().__init__(name);
        self.author = author;
        self.pageCount = pageCount;

    def print_information(self):
        print(f"the book name is {self.name}, \nthe book author is{self.author}, \nthe book pageCount is{self.pageCount}\n")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name);
        self.editor = editor;

    def print_information(self):
        print(f"the magazine name is {self.name}, "
              f"\nthe magazine editor is{self.editor}\n")


book = Book('Compartment No. 6','Rosa Liksom',192);
magazine = Magazine('Donald Duck', 'Aki Hyyppä');
book.print_information();
magazine.print_information()