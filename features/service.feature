Feature: Microservicio de ejemplo
  Como equipo de QA quiero validar los endpoints básicos para asegurar calidad antes del merge a main

  Scenario: Health responde ok
    When hago GET a "/health"
    Then el status code es 200
    And el json contiene "status" con "ok"

  Scenario: Sumar dos números
    When hago POST a "/sum" con json
      """
      {"a": 2, "b": 3}
      """
    Then el status code es 200
    And el campo "result" es 5

  Scenario: Error por datos inválidos
    When hago POST a "/sum" con json:
      """
      {"a": "x", "b": 3}
      """
    Then el status code es 422
