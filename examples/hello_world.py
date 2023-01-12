import grippy
from pydantic import BaseModel

app = grippy.App()

@app.rpc
def greet(times: int, name: str) -> str:
    return times * f"Hello {name}\n"

if __name__ == "__main__":
    print(app.proto)
    app.build()
    app.run()
