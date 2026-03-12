How the /profile API Works

After a user logs in successfully, the server generates and returns an access token (JWT). This token is used to authenticate the user when accessing protected APIs such as /profile.

When the /profile API is called, the access token is sent in the HTTP header as a Bearer token. FastAPI uses the OAuth2PasswordBearer dependency to extract this token from the request header.

<img width="682" height="56" alt="image" src="https://github.com/user-attachments/assets/e38c671f-f948-40a5-aa04-32b006877598" />

This tells FastAPI to look for the token in the header in the following format:

Authorization: Bearer <access_token>

Once the token is received, it is decoded using the secret key that was defined earlier in the application:

<img width="678" height="56" alt="image" src="https://github.com/user-attachments/assets/cd5cc07c-93cb-4337-b917-f88771c45b5f" />

During decoding, the server verifies the signature of the token using the same secret key that was used when the token was generated. If the token is valid and the signature matches, the payload data (such as the user's email) can be extracted.

After extracting the email from the token payload, the backend queries the database to retrieve the corresponding user details:
<img width="607" height="43" alt="image" src="https://github.com/user-attachments/assets/5f5b7560-dc46-4486-a36a-fb1add9faa17" />

Finally, the API returns the user's profile information.


How to Run the /profile API

Once the FastAPI server is running, the API can be tested using the curl command.
<img width="771" height="40" alt="image" src="https://github.com/user-attachments/assets/f4281a25-7aed-48d2-8b24-68a9dcc07f03" />

Explanation of the command:

curl → A tool used to send HTTP requests from the terminal
-X GET → Specifies the HTTP request method (GET)
-H → Used to send headers with the request
Authorization: Bearer <access_token> → Sends the JWT token required for authentication

<img width="496" height="386" alt="image" src="https://github.com/user-attachments/assets/daf8912a-b95c-40f8-b744-ec6833f15f69" />


