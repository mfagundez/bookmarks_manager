import csv
import bookmark

with open('tests/example.csv','r') as csvfile:
    spamReader = csv.reader(csvfile, delimiter=',')
    for row in spamReader:
        bookmarks = bookmark.Bookmarks()
        bookmarks.addBookmark(row)
    bookmarks.printBookmarks()
