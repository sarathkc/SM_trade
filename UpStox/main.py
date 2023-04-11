from upstox_api.api import *
# s = Session ('e2c3f76f-479e-4042-a4f3-646164517d28')
# s.set_redirect_uri ('http://localhost:3000/')
# s.set_api_secret ('s2b97brr12')

# # print (s.get_login_url())
# s.set_code ('KBGVGK')

access_token = 'eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI0UEE1MkEiLCJqdGkiOiI2NDJmYzAwMzNiYTRmNzZhMDcyMjEzNzciLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNBY3RpdmUiOnRydWUsInNjb3BlIjpbImludGVyYWN0aXZlIiwiaGlzdG9yaWNhbCJdLCJpYXQiOjE2ODA4NTA5NDcsImlzcyI6InVkYXBpLWdhdGV3YXktc2VydmljZSIsImV4cCI6MTY4MDkzOTE0N30.dztpoBp-Lm90BoMVyD7PXegbH3YuFVFsC5yhl45d17g'
print ('Received access_token: %s' % access_token)

u = Upstox ('e2c3f76f-479e-4042-a4f3-646164517d28', access_token)
print (u.get_profile())

# This is the ticket id:-7520011 for the ticket which I have raised.