Default Python Azure Function App starter package
--------------------------------------------------
Runtime: Python Azure Functions v2 programming model
Trigger: HTTP trigger

Files included:
- host.json: Azure Functions host configuration. Must be at the ZIP root.
- function_app.py: Sample HTTP-triggered function.
- requirements.txt: Python dependencies.
- .funcignore: Excludes local-only files from deployment.

Test endpoint after deployment:
https://<function-app-name>.azurewebsites.net/api/hello?name=Sonali

Note:
This ZIP is a simple starter package. Deploy it only to a Python Function App.
For .NET, Node.js, Java, or PowerShell, create a runtime-specific package instead.
