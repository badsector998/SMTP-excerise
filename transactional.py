from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

#build email
subject = "SendInBlue first Mail!"
sender = {"name":"Dadang Rokes", "email":"harddiskkosong@gmail.com"}
reply_to = {"name":"Dadang Rokes", "email":"harddiskkosong@gmail.com"}
to = [{"name":"Aprilito", "email":"aprilito.ikr@gmail.com"}]
html_content = """ 

<html>
<body>
<h1>This is my first email</h1>
<p>sent using send in blue service :).</p>
</body>
</html>


"""
params = {"parameter":"My Param Value", "subject":"New Subject"}
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
                                                to=to,
                                                reply_to=reply_to,
                                                html_content=html_content,
                                                sender=sender,
                                                subject=subject,
                                                )

try:
    api_response = api_instance.send_transac_email(send_smtp_email)
    print(api_response)
    
except ApiException as e:
    print("Error occured while sending the transaction SMTPApi -> send transac email : %s\n", e)