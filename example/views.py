from datetime import datetime

from django.http import HttpResponse

def index(request):
    return HttpResponse('''
    <html>
        <head>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        </head>
        <body class="bg-warning-subtle">
            <div class="container" style="text-align: center; margin-top: 10rem;">
                <h1>CIS-375 Hotel Management API</h1>
                <p>Coming Soon.</p>
                <p>
                    <a target="_blank" href="https://github.com/RyanAIIen/cis-375-proj-2024-03-api">
                        See the Code
                    </a>
                </p>
            </div>
        </body>
    </html>
    ''')
