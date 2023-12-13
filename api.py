# from fastapi import Body, FastAPI
# from data.users import users;

# app = FastAPI()

# @app.get("/api", description="Returns a hello message.")
# async def hello():
#   return {"message":"Hello, I'm alive!"}

# @app.get("/api/users", description="Returns all users available.")
# async def listUsers():
#   return users

# @app.get("/api/users/",description="Returns filtered list of users.")
# async def filterUsers(name: str):
#   print(f"name{name}")
#   filteredUsers = []
#   for user in users:
#     if user.get("name").casefold() == name.casefold():
#       filteredUsers.append(user)
  
#   return filteredUsers

# @app.post("/api/users", description="Creates a new user")
# async def createUser(newUser = Body()):
#   users.append(newUser)

# @app.put("/api/user", description="Updates an exisiting user.")
# async def updateUser(id: int, updatedUser = Body()):
#   for i in range(len(users)):
#     if users[i].get("id") == id:
#       users[i] = updatedUser
#       break

# @app.delete("/api/user", description="Deletes an existing user.")
# async def deleteUser(id: int):
#   for i in range(len(users)):
#     if users[i].get("id") == id:
#       users.pop(i)
#       break
