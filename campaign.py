from __future__ import print_function
import time
import datetime
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '-'

api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
tag = 'Notifcation'
sender = {"name": 'Dadang Rokes', "email": 'harddiskkosong@gmail.com'}
name = 'My First Campaign'
template_id= 10
scheduled_at = "2022-06-27T12:00:00+07:00"
subject = 'Campaign Test'
reply_to = 'harddiskkosong@gmail.com'
to_field = 'Dadang Rokes'
recipients = {"name": 'Aprilito', "email": 'aprilito.ikr@gmail.com'}
inline_image_activation = False
mirror_active = False
header = 'If you are not able to see this mail, click {here}'
footer = 'If you wish to unsubscribe from our newsletter, click {here}'
utm_campaign = 'My utm campaign value'
email_campaigns = sib_api_v3_sdk.CreateEmailCampaign(tag=tag, sender=sender, name=name, template_id=template_id, scheduled_at=scheduled_at, subject=subject, reply_to=reply_to, to_field=to_field, recipients=recipients, inline_image_activation=inline_image_activation,mirror_active=mirror_active, header=header, footer=footer, utm_campaign=utm_campaign) # CreateEmailCampaign | Values to create a campaign

try:
    api_response = api_instance.create_email_campaign(email_campaigns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->create_email_campaign: %s\n" % e)