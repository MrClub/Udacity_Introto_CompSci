# Write Python code that assigns to the
# variable url a string that is the value
# of the first URL that appears in a link
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url',
# and therefore still prints the same thing.

# page = contents of a web page
page = ('<div id="top_bin"><a href="http://github.com"><div id="top_content" class="width960">'
        '<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')

start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote + 1)
url1 = page[start_quote + 1:end_quote]
second_link = page.find('<a href=', start_link + 1)
second_quote = page.find('"', second_link)
second_end_quote = page.find('"', second_quote + 1)
url2 = page[second_quote + 1:second_end_quote]
print(url1)
print(url2)

# this is a test
