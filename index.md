<!DOCTYPE html>
<html lang="en">

<head>
    <title>Email Validation</title>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ"
        crossorigin="anonymous">
        <style>
    body {
      background-color: black;
    }

    body.container {
      opacity: 1;
    }
    h2 {
      color : white;
      text-align: center;
    }
    </style>
</head>

<body class="container">
    <div class="container">
        <div class="row justify-content-center">
          <h2>Registration in Covid-19 Pandemic Tracker <img Height="30" Weight="40" class="brand-img" src="{% static 'dist/img/logo.png' %}" alt="brand"
              style="width: 22px;" /></h2>
        </div>
        <div class="row justify-content-center">
            <div class="col-4">
                <div class="card">
                    <h4 class="card-header text-center">Register</h4>
                    <div class="card-block">
                        <form method="post" action="/register">
                            <div class="mx-auto text-center">
                                <input type="submit" value="Create Account" class="btn btn-primary">
                            </div>
                        </form>
                    </div>
                </div>
            </div>
            <div class="col-4">
                <div class="card">
                    <h4 class="card-header text-center">Login</h4>
                    <div class="card-block">
                        <form method="post" action="/login">
                            <div class="mx-auto text-center">
                                <input type="submit" value="Login" class="btn btn-primary">
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </script>
</body>

</html>
