import csv
import bookmark

with open('tests/example.csv', 'r') as csvfile:
    bookmarks = bookmark.Bookmarks()
    spamReader = csv.reader(csvfile, delimiter=',')
    for row in spamReader:
        singleBookmark = bookmark.Bookmark()
        singleBookmark.name = row[0]
        singleBookmark.url = row[1]
        singleBookmark.description = row[2]
        singleBookmark.path = row[3]
        bookmarks.addBookmark(singleBookmark)
    bookmarks.printBookmarks(",")
    