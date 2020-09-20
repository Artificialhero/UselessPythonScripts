import smtplib

ip = input("Enter mailservers ip: ")


 #TODO: More verbose.
 # Loop to send to many mail adresses.
 
 
#Make SMTP connection
conn = smtplib.SMTP(ip, 25)

#TLS based session. Unsure if works on all servers.
conn.starttls()

message = """
<p>Hello, you are awesome!</p>
"""

conn.quit()
