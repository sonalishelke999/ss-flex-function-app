import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="hello")
def hello(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = {}
        name = req_body.get("name")

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")

    return func.HttpResponse(
        "Hello from Azure Functions. Pass a name in the query string or request body for a personalized response.",
        status_code=200,
    )
