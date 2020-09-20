import smtplib

ip = input("Enter mailservers ip: ")


 #TODO: More verbose.
 # Loop to send to many mail adresses.
 # Allow user to simply run writemail.py <ip> <file>
 
 
#Make SMTP connection
conn = smtplib.SMTP(ip, 25)

#TLS based session. Unsure if works on all servers.
conn.starttls()

message = """
<p>Hello, you are awesome!</p>
"""
#Read in email adresses,emailFile
#Loop over each email adress in file



conn.sendmail(emailAdresses, message)

conn.quit()
