from fastapi import FastAPI, Path, HTTPException
from data.users import users
from models.user import User, UserRequest
from starlette import status

app = FastAPI()

@app.get("/api/users", description="Lists all users available.", status_code=status.HTTP_200_OK)
async def getAllUsers():
  return users

# In case we want to validate Query parameters we can use Query instead of Path.
@app.get("/api/user/{id}", description="Retrieve an user by id.", status_code=status.HTTP_200_OK)
async def getUserById(id: int = Path(gt = 0)):
  for user in users:
    if user.id == id:
      return user
    raise HTTPException(status_code=404, detail="User not found.") 

@app.post("/api/user", description="Creates an user in the DB.", status_code=status.HTTP_201_CREATED)
async def createUser(user: UserRequest):
  newUser = User(**user.model_dump())
  users.append(newUser)

@app.put("/api/user", description="Updates user.", status_code=status.HTTP_204_NO_CONTENT)
async def updateUser(user: UserRequest):
  userChanged = False
  for i in range(len(users)):
    if user.id == users[i].id:
      users[i] = user
      userChanged = True

  if not userChanged:
    raise HTTPException(status_code=404, detail="User not found." )


