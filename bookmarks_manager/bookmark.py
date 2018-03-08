class Bookmarks():
    def __init__(self):
        self.bookmarks = []
    
    # Adds a bookmark to the bookmarks list
    def addBookmark(self, bookmark):
        self.bookmarks.append(bookmark)

    # Prints all bookmarks to default stdout
    def printBookmarks(self):
        for bookmark in self.bookmarks:
            print(','.join(bookmark))
