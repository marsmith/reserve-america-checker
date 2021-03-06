#!/usr/bin/env python

import os
import sys
import mechanize
from bs4 import BeautifulSoup
import config
import secrets
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Find a campsite!')
parser.add_argument('date', type=str, help='Date in this format: "02/13/2021"' )
parser.add_argument('duration', type=int, help='Legnth of stay in days')
parser.add_argument('area', type=str, choices=config.campgrounds.keys(), help='Search area group, setup in config.py')
parser.add_argument('rv_length', type=int, help='RV length, set to "0" for all')
parser.add_argument('email', type=bool, help='Do you want email? need secrets.py to function')
args = parser.parse_args()

DATE = args.date
DURATION = args.duration
AREA = args.area
LENGTH = args.rv_length
EMAIL = args.email
USER_AGENT = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.33 Safari/537.36')

# Try to import Twilio
try:
    from twilio.rest import Client as TwilioClient
except ImportError:
    TwilioClient = None

# Optional Twilio configuration
twilio_account_sid = secrets.twilio_account_sid
twilio_auth_token = secrets.twilio_auth_token
twilio_from_number = secrets.twilio_from_number
twilio_to_number = secrets.twilio_to_number
has_twilio = all([
    TwilioClient,
    twilio_account_sid,
    twilio_auth_token,
    twilio_from_number,
    twilio_to_number,
])

def send_sms(message):
    if not has_twilio:
        return

    #msg = "{}. {}".format(message, url)
    msg = message

    client = TwilioClient(twilio_account_sid, twilio_auth_token)
    
    for to_number in twilio_to_number:
        message = client.messages.create(to=to_number, from_=twilio_from_number, body=msg)

def sendEmail(subject, text):
    #https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/

    # Python code to illustrate Sending mail with attachments 
    # from your Gmail account  

    # libraries to be imported 
    import smtplib 
    from email.mime.multipart import MIMEMultipart 
    from email.mime.text import MIMEText 
    from email.mime.base import MIMEBase 
    from email import encoders

    fromaddr = secrets.email
    toaddr = secrets.email

    # instance of MIMEMultipart 
    msg = MIMEMultipart() 

    # storing the senders email address   
    msg['From'] = fromaddr 

    # storing the receivers email address  
    msg['To'] = toaddr 

    # storing the subject  
    msg['Subject'] = subject

    # string to store the body of the mail 
    body = text

    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 

    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 

    # start TLS for security 
    s.starttls() 

    # Authentication 
    s.login(fromaddr, secrets.password) 

    # Converts the Multipart msg into a string 
    text = msg.as_string() 

    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 

    # terminating the session 
    s.quit() 

def send_results(result_date, name, hits, ra_url):
	subject = name + " " + result_date + " Campsite Found!!"
	message = "{}, found available sites at {}: {}  \r\nBook now at: {}".format(result_date, name,', '.join(hits), ra_url)
	print(message)
	sendEmail(subject, message)
	send_sms(subject)

def run():
    print("SCRIPT STARTING")

    def parse_page(page):

        # Scrape result
        soup = BeautifulSoup(page, "html.parser")
        table = soup.findAll("div", {"id": "shoppingitems"})

        if table:
            found_unavailable = False

            #print(table)
            rows = table[0].findAll("div", {"class": "br"})

            #loop over table, skipping first row (header)
            for row in rows[1:]:
                cells = row.findAll("div", {"class": "td"})
                l = len(cells)
                
                label = cells[0].findAll("div", {"class": "siteListLabel"})[0].text

                siteType = cells[2].text

                #could have string like: '15 Back-In'
                equip_length_driveway = cells[4].text.split(' ')

                length = 0
                driveway = ''

                #print('equip_length_driveway', equip_length_driveway)

                #so many permutations of possibilities for this field, ugh
                if len(equip_length_driveway) == 1:
                    #if its length one and is a number, its a length
                    if equip_length_driveway[0].isnumeric():
                        length = equip_length_driveway[0]

                    #otherwise its a driveway
                    else:
                        driveway = equip_length_driveway[0]

                #if we have two items, it should be a length and a driveway
                if len(equip_length_driveway) == 2:
                    if len(equip_length_driveway[0]) > 0:
                        length = equip_length_driveway[0]
                    else:
                        length = 0
                    driveway = equip_length_driveway[1]

                status = cells[l - 1].text

                #make sure we store any available 'not available' sites
                available = False

                #print('sitetype:', label, siteType, length, driveway)

                #are we looking for RV site
                if LENGTH > 0:
                    #print('searching RV sites')

                    if status.startswith('available') and siteType != 'Tent Only' and int(length) > LENGTH:
                    #if status.startswith('available'):
                        #print('sitetype:', label, siteType, length, driveway)
                        available = True

                    else:
                        found_unavailable = True
                            
                #SEARCHING TENT SITES
                else:
                    #print('searching tent sites')
                    if status.startswith('available'):
                        available = True

                    else:
                        found_unavailable = True

                if available:

                    #print('sitetype:', label, siteType, length, driveway)

                    #if there are preferred sites defined:
                    if 'preferred_sites' in campground:

                        #print('found available site:', label)
                        if label in campground['preferred_sites']:
                            #print('found preferred site:', label, len(total_hits))
                            total_hits.append(label)

                    else:
                        total_hits.append(label)

            #if we found any unavailable sites then were done, because its sorted by availability
            if found_unavailable:
                print('Were done here')
            else:
                print('Looking through additional pages...')

                for link in br.links():
                    #print(link)

                    attrs = dict(link.attrs) 
                    if 'id' in attrs:
                        
                        if (attrs['id'] == 'resultNext_top'):
                            #print('has id:', attrs)
                            response = br.follow_link(link)

                            #recursively call self
                            parse_page(response)


    for campground in config.campgrounds[AREA]:
        total_hits = []

        # Create browser
        br = mechanize.Browser()

        # Browser options
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        br.addheaders = [('User-agent', USER_AGENT)]
        html = br.open(campground['ra_url'])

        #get campground name
        page = BeautifulSoup(html, "html.parser")
        span = page.find('span', id='cgroundName')
        name = span.text
        page.decompose()
        
        # Fill out form
        br.select_form(name="unifSearchForm")
        br.form.set_all_readonly(False)  # allow changing the .value of all controls
        br.form["campingDate"] = DATE
        br.form["lengthOfStay"] = str(DURATION)
        response = br.submit()

        #initial kickoff
        print('Processing:', name)
        parse_page(response)

        if len(total_hits) > 0:
            print(DATE, name, total_hits, campground['ra_url'])

            if EMAIL:
                send_results(DATE, name, total_hits, campground['ra_url'])
        else:
            message = 'No sites found for date: ' + DATE
            #sendEmail(message)
            print(message)

if __name__ == '__main__':
    run()
