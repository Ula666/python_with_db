import requests

class NewBooks:
    def __init__(self):
        self.url = "https://openlibrary.org/books/"
        self.greetings()
        self.books = input("Please enter book id that you're interested in: ")
       # self.url_arg = self.url + self.books
        #self.retrieve_info()

    def greetings(self):
        print("Hello User!")



# OL7353617M


    # def retrieve_info(self):
    #     books = input("Please enter book id that you're interested in: ")
    #     print(self.url_arg)

    def check_status(self):
        url_arg = self.url + self.books
        print(url_arg)
        status = requests.get(url_arg).status_code
        if status == 200:
            print("The website is running" +str(status))
        else:
            print("Something wrong")


book = NewBooks()
book.greetings()
book.check_status()



