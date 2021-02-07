# POSTMORTEM

The day 14/12/2020 at 04:23am PST the servers of website1 have issues give us back the response of an error 500 and 503. This type of errors belong to the class of codes HTTP that inform the incapacity of the server to process a request and the message in the page is "service not available". The service was restored after debugging at 04:30am PST, That was fast, thank you so much!

## Debugging timeline

04:24 -> Used "ps aux" to obtain the information of the process we are running

04:24 -> Checking the apache2 configuration

04:26 -> Checking the folder of sites-available in /var/www/html/

04:28 -> Debugging the code inside the sites-available

04:30 -> Fixing the port of the visrtual host to :80

04:30 -> Testing with command curl in the server: response 200 (fixed)

## Problem and solution

