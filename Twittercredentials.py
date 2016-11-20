import tweepy

consumer_key = "DkmRN2ZXmOK2DHDuPAs7bbOhe";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "hP0Nc1UUgCIM44iA1ckfB0VMRTP6AbYxRnvxQvhgjgQMtIPiJm";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "799413943521447936-tcGTjdjxnW4hy4SlpKs81IRTZFw1dGe";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "cdOnNxznkqrQoSbj8xYCVn5jxtHoZHJenHerRiJDZAo02";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



