class Bookmarks():
    def __init__(self):
        self.bookmarks = []
    
    # Adds a single bookmark to the bookmarks list
    def addBookmark(self, singleBookmark):
        self.bookmarks.append(singleBookmark)

    # Prints all bookmarks to default stdout
    def printBookmarks(self, separator):
        for singleBookmark in self.bookmarks:
            singleBookmark.printf(separator)

class Bookmark():
    def __init__(self):
        self.name=""
        self.url=""
        self.description=""
        self.path=""
        self.status=False

    def printf(self, separator):
        print(self.name + separator + self.url + separator +
              self.description + separator + self.path + separator + str(self.status))
