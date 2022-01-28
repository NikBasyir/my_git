from typing import Optional

from fastapi import FastAPI
import uvicorn

app = FastAPI()

num1 = 1.5
num2 = 2.5

sum = num1 + num2

#print('the sum of {0} and {1} is {2}'.format(num1, num2, sum))

@app.get("/")
def read_root():
	return {'the sum of {0} and {1} is {2}'.format(num1, num2, sum)}



if __name__ == '__main__':
	uvicorn.run(app, port=8000, host="0.0.0.0")
