from app import app

@app.route('/')
@app.route('/index')
def index():
    return """
<!doctype html>
<html  >

<head>
  <meta charset="utf-8">
  <title></title>


</head>

<body>
    <h1 style="width: 100%; text-align: center; font-family: sans-serif">Hello, Hacktoberfest!</h1>
</body>

</html>
    """