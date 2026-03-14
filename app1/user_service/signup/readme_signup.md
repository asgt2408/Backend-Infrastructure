password_bytes = user.password.encode("utf-8")[:72]
hashed_password = pwd_context.hash(password_bytes.decode("utf-8", "ignore"))


