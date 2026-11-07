
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <title>Cestovní Portál</title>
</head>
<body>
    <h1>Vítejte na našem cestovním portálu!</h1>
    <p>Aktuální čas a datum: <strong>{{ aktualni_cas|date:"d.m.Y H:i:s" }}</strong></p>

    <div>
        {% if user.is_authenticated %}
            <p>Přihlášen uživatel: <strong>{{ user.username }}</strong> |
            <form action="{% url 'logout' %}" method="post" style="display:inline;">
                {% csrf_token %}
                <button type="submit">Odhlásit se</button>
            </form></p>
        {% else %}
            <a href="{% url 'login' %}">Přihlásit se</a>
        {% endif %}
    </div>

    <hr>
    <nav>
        <ul>
            <li><a href="{% url 'vyber_zeme' %}">Vybrat zemi a zobrazit itineráře</a></li>
            <li><a href="{% url 'chat_admin' %}">Napsat administrátorovi</a></li>
        </ul>
    </nav>
</body>
</html>
