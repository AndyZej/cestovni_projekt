
<!DOCTYPE html>
<html lang="cs">
<head><meta charset="UTF-8"><title>Přihlášení</title></head>
<body>
    <h1>Přihlášení do systému</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Přihlásit</button>
    </form>
    <p><a href="{% url 'domov' %}">Zpět na úvodní stránku</a></p>
</body>
</html>
