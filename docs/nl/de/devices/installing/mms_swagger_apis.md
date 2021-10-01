{
    "swagger": "2.0",
    "info": {
      "description": "Diese Dokumentation behandelt die Richtlinienressource für IBM Multicloud Manager (policy.mcm.ibm.com).\nDie Richtlinienressource für IBM Multicloud Manager bietet vier mögliche Anforderungen: Erstellung, Abfrage aller Richtlinien, Abfrage einer einzelnen Richtlinie und Löschung.,
      "version": "3.2.1",
      "title": "Dokumentation zur Richtlinien-API für IBM Multicloud Manager",
      "termsOfService": "http://swagger.io/terms/",
      "contact": {
        "email": "apiteam@swagger.io"
      },
      "license": {
        "name": "Apache 2.0",
        "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
      }
    },
    "basePath": "/kubernetes/apis",
    "tags": [
      {
        "name": "Policy.mcm.ibm.com",
        "description": "Erstellt und verwaltet Richtlinien mit der Richtlinienressource."
      }
    ],
    "schemes": [
      "https",
      "http"
    ],
    "paths": {
      "/policy.mcm.ibm.com/v1alpha1/namespaces/{namespace}/policies": {
        "post": {
          "tags": [
            "Policy.mcm.ibm.com"
          ],
          "summary": "Richtlinie erstellen",
          "description": "Erstellt eine Richtlinie, um die Governance und das Risiko für den Cluster zu melden und zu validieren.",
          "operationId": "createPolicy",
          "consumes": [
            "application/yaml"
          ],
          "parameters": [
            {
              "in": "body",
              "name": "body",
              "description": "Parameter für die Beschreibung der zu erstellenden Richtlinie.",
              "required": true,
              "schema": {
                "$ref": "#/definitions/Policy"
              }
            },
            {
              "in": "path",
              "name": "namespace",
              "description": "Der Namensbereich, den Sie verwenden wollen, z. B. 'default'.",
              "required": true,
              "type": "string"
            },
            {
              "name": "COOKIE",
              "in": "header",
              "description": "Berechtigung: Träger {ZUGRIFFSTOKEN}; ZUGRIFFSTOKEN ist das Benutzerzugriffstoken.",
              "type": "string",
              "required": true
            }
          ],
          "responses": {
            "200": {
              "description": "Erfolg"
            },
            "403": {
              "description": "Zugriff nicht zulässig"
            },
            "404": {
              "description": "Ressource nicht gefunden"
            },
            "500": {
              "description": "Interner Servicefehler"
            },
            "503": {
              "description": "Service nicht verfügbar"
            }
          }
        },
        "get": {
          "tags": [
            "Policy.mcm.ibm.com"
          ],
          "summary": "Alle Richtlinien abfragen",
          "description": "Fragt Ihre Richtlinien nach weiteren Details ab.",
          "operationId": "queryPolicies",
          "consumes": [
            "application/yaml"
          ],
          "parameters": [
            {
              "in": "path",
              "name": "namespace",
              "description": "Der Namensbereich, den Sie verwenden wollen, z. B. 'default'.",
              "required": true,
              "type": "string"
            },
            {
              "name": "COOKIE",
              "in": "header",
              "description": "Berechtigung: Träger {ZUGRIFFSTOKEN}; ZUGRIFFSTOKEN ist das Benutzerzugriffstoken.",
              "type": "string",
              "required": true
            }
          ],
          "responses": {
            "200": {
              "description": "Erfolg"
            },
            "403": {
              "description": "Zugriff nicht zulässig"
            },
            "404": {
              "description": "Ressource nicht gefunden"
            },
            "500": {
              "description": "Interner Servicefehler"
            },
            "503": {
              "description": "Service nicht verfügbar"
            }
          }
        }
      },
      "/policy.mcm.ibm.com/v1alpha1/namespaces/{namespace}/policies/{policy_name}": {
        "get": {
          "tags": [
            "Policy.mcm.ibm.com"
          ],
          "summary": "Einzelne Richtlinie abfragen",
          "description": "Fragt eine einzelne Richtlinie nach weiteren Details ab.",
          "operationId": "queryPolicy",
          "parameters": [
            {
              "name": "policy_name",
              "in": "path",
              "description": "Der Name der Richtlinie, die Sie abfragen wollen.",
              "required": true,
              "type": "string"
            },
            {
              "in": "path",
              "name": "namespace",
              "description": "Der Namensbereich, den Sie verwenden wollen, z. B. 'default'.",
              "required": true,
              "type": "string"
            },
            {
              "name": "COOKIE",
              "in": "header",
              "description": "Berechtigung: Träger {ZUGRIFFSTOKEN}; ZUGRIFFSTOKEN ist das Benutzerzugriffstoken.",
              "type": "string",
              "required": true
            }
          ],
          "responses": {
            "200": {
              "description": "Erfolg"
            },
            "403": {
              "description": "Zugriff nicht zulässig"
            },
            "404": {
              "description": "Ressource nicht gefunden"
            },
            "500": {
              "description": "Interner Servicefehler"
            },
            "503": {
              "description": "Service nicht verfügbar"
            }
          }
        },
        "delete": {
          "tags": [
            "Policy.mcm.ibm.com"
          ],
          "summary": "Richtlinie löschen",
          "description": "",
          "operationId": "deletePolicy",
          "parameters": [
            {
              "name": "policy_name",
              "in": "path",
              "description": "Der Name der Richtlinie, die Sie löschen wollen.",
              "required": true,
              "type": "string"
            },
            {
              "in": "path",
              "name": "namespace",
              "description": "Der Namensbereich, den Sie verwenden wollen, z. B. 'default'.",
              "required": true,
              "type": "string"
            },
            {
              "name": "COOKIE",
              "in": "header",
              "description": "Berechtigung: Träger {ZUGRIFFSTOKEN}; ZUGRIFFSTOKEN ist das Benutzerzugriffstoken.",
              "type": "string",
              "required": true
            }
          ],
          "responses": {
            "200": {
              "description": "Erfolg"
            },
            "403": {
              "description": "Zugriff nicht zulässig"
            },
            "404": {
              "description": "Ressource nicht gefunden"
            },
            "500": {
              "description": "Interner Servicefehler"
            },
            "503": {
              "description": "Service nicht verfügbar"
            }
          }
        }
      }
    },
    "definitions": {
      "Policy": {
        "type": "object",
        "required": [
          "apiVersion",
          "kind",
          "metadata",
          "spec"
        ],
        "properties": {
          "apiVersion": {
            "type": "string"
          },
          "kind": {
            "type": "string"
          },
          "metadata": {
            "type": "object"
          },
          "spec": {
            "type": "object",
            "properties": {
              "remediationAction": {
                "type": "string"
              },
              "namespaces": {
                "type": "object",
                "properties": {
                  "include": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "exclude": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  }
                }
              },
              "roleTemplates": {
                "type": "object",
                "properties": {
                  "kind": {
                    "type": "string"
                  },
                  "apiVersion": {
                    "type": "string"
                  },
                  "complianceType": {
                    "type": "string"
                  },
                  "metadata": {
                    "type": "object"
                  },
                  "selector": {
                    "type": "object",
                    "properties": {
                      "matchLabels": {
                        "type": "object"
                      }
                    }
                  },
                  "rules": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "complianceType": {
                          "type": "string"
                        },
                        "PolicyRule": {
                          "type": "object",
                          "properties": {
                            "apiGroups": {
                              "type": "array",
                              "items": {
                                "type": "string"
                              }
                            },
                            "resources": {
                              "type": "array",
                              "items": {
                                "type": "string"
                              }
                            },
                            "verbs": {
                              "type": "array",
                              "items": {
                                "type": "string"
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "example": {
          "apiVersion": "policy.mcm.ibm.com/v1alpha1",
          "kind": "Policy",
          "metadata": {
            "name": "test-policy-swagger",
            "description": "API-Swagger-Beispielinhalt für die Richtlinienressource."
          },
          "spec": {
            "remediationAction": "enforce",
            "namespaces": {
              "include": [
                "default"
              ],
              "exclude": [
                "kube*"
              ]
            },
            "roleTemplates": {
              "kind": "RoleTemplate",
              "apiVersion": "roletemplate.mcm.ibm.com/v1alpha1",
              "complianceType": "musthave",
              "metadata": {
                "namespace": null,
                "name": "test-role"
              },
              "selector": {
                "matchLabels": {
                  "cloud": "IBM"
                }
              }
            },
            "rules": [
              {
                "complianceType": "musthave",
                "PolicyRule": {
                  "apiGroups": [
                    "extensions",
                    "apps"
                  ],
                  "resources": [
                    "deployments"
                  ],
                  "verbs": [
                    "get",
                    "list",
                    "watch",
                    "delete"
                  ]
                }
              },
              {
                "complianceType": "mustnothave",
                "PolicyRule": {
                  "apiGroups": [
                    "core"
                  ],
                  "resources": [
                    "pods"
                  ],
                  "verbs": [
                    "create",
                    "update",
                    "patch"
                  ]
                }
              },
              {
                "PolicyRule": null,
                "apiGroups": [
                  "core"
                ],
                "resources": [
                  "secrets"
                ],
                "verbs": [
                  "get",
                  "watch",
                  "list",
                  "create",
                  "delete",
                  "update",
                  "patchß"
                ]
              }
            ]
          }
        }
      }
    },
    "externalDocs": {
      "description": "Hier erfahren Sie mehr über Swagger."
    },
    "url": "http://swagger.io"
  }
