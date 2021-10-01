{
    "swagger": "2.0",
  "info": {
      "description": "Esta documentación es para el recurso de política para IBM Multicloud Manager (policy.mcm.ibm.com). \nEl recurso de política de IBM Multicloud Manager tiene cuatro posibles solicitudes: crear, consultar todas las políticas, consultar una única política y suprimir.",
      "version": "3.2.1",
      "title": "Documentación de API de política de IBM Multicloud Manager",
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
        "description": "Crear y gestionar políticas con el recurso de política."
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
          "summary": "Crear una política",
          "description": "Crear una política para informar del gobierno y riesgo de clúster y validarlos.",
          "operationId": "createPolicy",
          "consumes": [
            "application/yaml"
          ],
          "parameters": [
            {
              "in": "body",
              "name": "body",
              "description": "Parámetros que describen la política que se debe crear.",
              "required": true,
              "schema": {
                "$ref": "#/definitions/Policy"
              }
            },
            {
              "in": "path",
              "name": "namespace",
              "description": "Espacio de nombre que desea utilizar, por ejemplo, default.",
              "required": true,
              "type": "string"
            },
            {
              "name": "COOKIE",
              "in": "header",
              "description": "Autorización: el portador {ACCESS_TOKEN} ; ACCESS_TOKEN es la señal de acceso de usuario.",
              "type": "string",
              "required": true
            }
          ],
          "responses": {
            "200": {
              "description": "Satisfactorio"
            },
            "403": {
              "description": "Acceso prohibido"
            },
            "404": {
              "description": "Recurso no encontrado"
            },
            "500": {
              "description": "Error de servicio interno"
            },
            "503": {
              "description": "Servicio no disponible"
            }
          }
        },
        "get": {
          "tags": [
            "Policy.mcm.ibm.com"
          ],
          "summary": "Consultar todas las políticas",
          "description": "Consultar las políticas para obtener más detalles.",
          "operationId": "queryPolicies",
          "consumes": [
            "application/yaml"
          ],
          "parameters": [
            {
              "in": "path",
              "name": "namespace",
              "description": "Espacio de nombre que desea utilizar, por ejemplo, default.",
              "required": true,
              "type": "string"
            },
            {
              "name": "COOKIE",
              "in": "header",
              "description": "Autorización: el portador {ACCESS_TOKEN} ; ACCESS_TOKEN es la señal de acceso de usuario.",
              "type": "string",
              "required": true
            }
          ],
          "responses": {
            "200": {
              "description": "Satisfactorio"
            },
            "403": {
              "description": "Acceso prohibido"
            },
            "404": {
              "description": "Recurso no encontrado"
            },
            "500": {
              "description": "Error de servicio interno"
            },
            "503": {
              "description": "Servicio no disponible"
            }
          }
        }
      },
      "/policy.mcm.ibm.com/v1alpha1/namespaces/{namespace}/policies/{policy_name}": {
        "get": {
          "tags": [
            "Policy.mcm.ibm.com"
          ],
          "summary": "Consultar una única política",
          "description": "Consultar una única política para obtener más detalles.",
          "operationId": "queryPolicy",
          "parameters": [
            {
              "name": "policy_name",
              "in": "path",
              "description": "Nombre de la política que desea consultar.",
              "required": true,
              "type": "string"
            },
            {
              "in": "path",
              "name": "namespace",
              "description": "Espacio de nombre que desea utilizar, por ejemplo, default.",
              "required": true,
              "type": "string"
            },
            {
              "name": "COOKIE",
              "in": "header",
              "description": "Autorización: el portador {ACCESS_TOKEN} ; ACCESS_TOKEN es la señal de acceso de usuario.",
              "type": "string",
              "required": true
            }
          ],
          "responses": {
            "200": {
              "description": "Satisfactorio"
            },
            "403": {
              "description": "Acceso prohibido"
            },
            "404": {
              "description": "Recurso no encontrado"
            },
            "500": {
              "description": "Error de servicio interno"
            },
            "503": {
              "description": "Servicio no disponible"
            }
          }
        },
        "delete": {
          "tags": [
            "Policy.mcm.ibm.com"
          ],
          "summary": "Suprimir una política",
          "description": "",
          "operationId": "deletePolicy",
          "parameters": [
            {
              "name": "policy_name",
              "in": "path",
              "description": "Nombre de la política que desea suprimir.",
              "required": true,
              "type": "string"
            },
            {
              "in": "path",
              "name": "namespace",
              "description": "Espacio de nombre que desea utilizar, por ejemplo, default.",
              "required": true,
              "type": "string"
            },
            {
              "name": "COOKIE",
              "in": "header",
              "description": "Autorización: el portador {ACCESS_TOKEN} ; ACCESS_TOKEN es la señal de acceso de usuario.",
              "type": "string",
              "required": true
            }
          ],
          "responses": {
            "200": {
              "description": "Satisfactorio"
            },
            "403": {
              "description": "Acceso prohibido"
            },
            "404": {
              "description": "Recurso no encontrado"
            },
            "500": {
              "description": "Error de servicio interno"
            },
            "503": {
              "description": "Servicio no disponible"
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
            "description": "Contenido de Swagger de API de ejemplo para el recurso de política."
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
      "description": "Más información sobre Swagger."
    },
    "url": "http://swagger.io"
  }
