page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

start_link = page.find('<a href=')
start_quote = page.find('"',start_link)
end_quote = page.find('"',start_quote+1)
url = page[start_quote+1:end_quote]
print (url)
