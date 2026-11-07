
<!DOCTYPE html>
<html lang="cs">
<head><meta charset="UTF-8"><title>Výběr země</title></head>
<body>
    <h1>Vyberte si zemi</h1>
    <ul>
        {% for z in vsechny_zeme %}
            <li>
                <strong>{{ z.nazev }}</strong> -
                <a href="{% url 'itinerar' z.id %}">Zobrazit itinerář</a>
            </li>
        {% empty %}
            <li>Zatím nejsou přidány žádné země. Přidejte je přes administraci.</li>
        {% endfor %}
    </ul>
    <p><a href="{% url 'domov' %}">Zpět na úvodní stránku</a></p>
</body>
</html>
