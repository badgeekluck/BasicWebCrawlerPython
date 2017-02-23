page =('<div id="bin"><div id="content" class="width960">'
'<div class="google float-left"><a href="http://www.google.com">')

first_link = page.find('<a href=')
start_quote = page.find('"',first_link)
end_quote = page.find('"',start_quote+1)
url = page[start_quote+1:end_quote]
print (url)
