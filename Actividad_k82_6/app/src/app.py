from flask import Flask, request, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Métricas de Prometheus
disparos_totales = Counter(name='total_requests_http',documentation='Número total de disparos realizados',labelnames=["method","endpoint","http_status"])
disparos_acertados = Counter(name='disparos_acertados',documentation='Número total de disparos acertados',labelnames=["method","endpoint","http_status"])
disparos_fallados = Counter(name='disparos_fallados',documentation='Número total de disparos fallados',labelnames=["method","endpoint","http_status"])

@app.route("/metrics")
def get_metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

# Función para registrar los disparos
@app.post("/send_stat")
def registrar_disparo():
    data = request.get_json()
    # Extremos info de la request
    acierto = data.get("acierto", False)
    method = data.get("method", "POST")
    endpoint = data.get("endpoint", "/send_stat")
    status_code = data.get("status_code", 200)
    """Registrar si el disparo fue acertado o fallado en las métricas"""
    disparos_totales.labels(method, endpoint, status_code).inc()  # Incrementar contador de disparos totales
    if acierto:
        disparos_acertados.labels(method, endpoint, status_code).inc()  # Incrementar contador de aciertos
    else:
        disparos_fallados.labels(method, endpoint, status_code).inc()  # Incrementar contador de fallos
    return jsonify({"message": "Estadística registrada", "acierto": acierto}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)