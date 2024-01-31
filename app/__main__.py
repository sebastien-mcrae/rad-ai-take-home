import uvicorn


def main():
    uvicorn.run("app.application:app", host="0.0.0.0", port=8000, reload=False)


if __name__ == "__main__":
    main()
