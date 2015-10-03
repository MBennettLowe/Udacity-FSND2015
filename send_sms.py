from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACc3d41cf736108687468da47659dc568f"
auth_token  = "795ca7fa93f75994833de66de4984c09"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Moe Lowe, Full Stack Developer",
    to="+14437036192",    # Replace with your phone number
    from_="+14438154207") # Replace with your Twilio number
print message.sid
