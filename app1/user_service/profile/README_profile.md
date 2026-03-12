Since, we know, we are getting access token after logging in. So, when running the /Profile api, it get the access token as a header (bearer token), and it authorizes through using 
OAuth2PasswordBearer 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user_service/login")

from the header and we will decode the token: (payload = jwt.decode(token,SECRET_KEY,algorithms=["HS256"]))

and from the secret key, we have declared earlier and it matches automatically and when matching is successfull,
data is extracted and then run the database query for exact details. (user = db.query(User).filter(User.email == email).first())


!! How to run this API !!

As soon as the server gets on: we will run 

curl -X GET "<I.P Address>" -H "Authorization: Bearer <Access-Token>"

{
	curl -> tool to send HTTP request
	-X GET -> Request emthod
	-H -> Header
} 
