{
    "swagger": "2.0",
  "info": {
      "description": "此文档适用于 IBM Multicloud Manager 的策略资源 (policy.mcm.ibm.com)。\nIBM Multicloud Manager 策略资源有四个可能的请求：创建、查询所有策略、查询单个策略和删除。",
      "version": "3.2.1",
      "title": "IBM Multicloud Manager policy API 文档",
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
        "description": "使用此策略资源创建和管理策略。"
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
          "summary": "创建策略",
          "description": "创建策略以报告和验证集群管理和风险。",
          "operationId": "createPolicy",
          "consumes": [
            "application/yaml"
          ],
          "parameters": [
            {
              "in": "主体",
              "name": "body",
              "description": "描述要创建的策略的参数。",
              "required": true,
              "schema": {
                "$ref": "#/definitions/Policy"
              }
            },
            {
              "in": "路径",
              "name": "namespace",
              "description": "要使用的名称空间，例如，缺省名称空间。",
              "required": true,
              "type": "字符串"
            },
            {
              "name": "COOKIE",
              "in": "头",
              "description": "授权：持有者 {ACCESS_TOKEN}；ACCESS_TOKEN 是用户访问令牌。",
              "type": "字符串",
              "required": true
            }
          ],
          "responses": {
            "200": {
              "description": "成功"
            },
            "403": {
              "description": "禁止访问"
            },
            "404": {
              "description": "找不到资源"
            },
            "500": {
              "description": "内部服务错误"
            },
            "503": {
              "description": "服务不可用"
            }
          }
        },
        "get": {
          "tags": [
            "Policy.mcm.ibm.com"
          ],
          "summary": "查询所有策略",
          "description": "查询您的策略以获取更多详细信息。",
          "operationId": "queryPolicies",
          "consumes": [
            "application/yaml"
          ],
          "parameters": [
            {
              "in": "路径",
              "name": "namespace",
              "description": "要使用的名称空间，例如，缺省名称空间。",
              "required": true,
              "type": "字符串"
            },
            {
              "name": "COOKIE",
              "in": "头",
              "description": "授权：持有者 {ACCESS_TOKEN}；ACCESS_TOKEN 是用户访问令牌。",
              "type": "字符串",
              "required": true
            }
          ],
          "responses": {
            "200": {
              "description": "成功"
            },
            "403": {
              "description": "禁止访问"
            },
            "404": {
              "description": "找不到资源"
            },
            "500": {
              "description": "内部服务错误"
            },
            "503": {
              "description": "服务不可用"
            }
          }
        }
      },
      "/policy.mcm.ibm.com/v1alpha1/namespaces/{namespace}/policies/{policy_name}": {
        "get": {
          "tags": [
            "Policy.mcm.ibm.com"
          ],
          "summary": "查询单个策略",
          "description": "查询单个策略以获取更多详细信息。",
          "operationId": "queryPolicy",
          "parameters": [
            {
              "name": "policy_name",
              "in": "路径",
              "description": "要查询的策略的名称。",
              "required": true,
              "type": "字符串"
            },
            {
              "in": "路径",
              "name": "namespace",
              "description": "要使用的名称空间，例如，缺省名称空间。",
              "required": true,
              "type": "字符串"
            },
            {
              "name": "COOKIE",
              "in": "头",
              "description": "授权：持有者 {ACCESS_TOKEN}；ACCESS_TOKEN 是用户访问令牌。",
              "type": "字符串",
              "required": true
            }
          ],
          "responses": {
            "200": {
              "description": "成功"
            },
            "403": {
              "description": "禁止访问"
            },
            "404": {
              "description": "找不到资源"
            },
            "500": {
              "description": "内部服务错误"
            },
            "503": {
              "description": "服务不可用"
            }
          }
        },
        "delete": {
          "tags": [
            "Policy.mcm.ibm.com"
          ],
          "summary": "删除策略",
          "description": "",
          "operationId": "deletePolicy",
          "parameters": [
            {
              "name": "policy_name",
              "in": "路径",
              "description": "要删除的策略的名称。",
              "required": true,
              "type": "字符串"
            },
            {
              "in": "路径",
              "name": "namespace",
              "description": "要使用的名称空间，例如，缺省名称空间。",
              "required": true,
              "type": "字符串"
            },
            {
              "name": "COOKIE",
              "in": "头",
              "description": "授权：持有者 {ACCESS_TOKEN}；ACCESS_TOKEN 是用户访问令牌。",
              "type": "字符串",
              "required": true
            }
          ],
          "responses": {
            "200": {
              "description": "成功"
            },
            "403": {
              "description": "禁止访问"
            },
            "404": {
              "description": "找不到资源"
            },
            "500": {
              "description": "内部服务错误"
            },
            "503": {
              "description": "服务不可用"
            }
          }
        }
      }
    },
    "definitions": {
      "Policy": {
        "type": "对象",
        "required": [
          "apiVersion",
          "kind",
          "metadata",
          "spec"
        ],
        "properties": {
          "apiVersion": {
            "type": "字符串"
          },
          "kind": {
            "type": "字符串"
          },
          "metadata": {
            "type": "对象"
          },
      "spec": {
            "type": "对象",
            "properties": {
              "remediationAction": {
                "type": "字符串"
              },
              "namespaces": {
                "type": "对象",
                "properties": {
                  "include": {
                    "type": "数组",
                    "items": {
                      "type": "字符串"
                    }
                  },
                  "exclude": {
                    "type": "数组",
                    "items": {
                      "type": "字符串"
                    }
                  }
                }
              },
              "roleTemplates": {
                "type": "对象",
                "properties": {
                  "kind": {
                    "type": "字符串"
                  },
                  "apiVersion": {
                    "type": "字符串"
                  },
                  "complianceType": {
                    "type": "字符串"
                  },
                  "metadata": {
                    "type": "对象"
                  },
                  "selector": {
                    "type": "对象",
                    "properties": {
                      "matchLabels": {
                        "type": "对象"
                      }
                    }
                  },
                  "rules": {
                    "type": "数组",
                    "items": {
                      "type": "对象",
                      "properties": {
                        "complianceType": {
                          "type": "字符串"
                        },
                        "PolicyRule": {
                          "type": "对象",
                          "properties": {
                            "apiGroups": {
                              "type": "数组",
                              "items": {
                                "type": "字符串"
                              }
                            },
                            "resources": {
                              "type": "数组",
                              "items": {
                                "type": "字符串"
                              }
                            },
                            "verbs": {
                              "type": "数组",
                              "items": {
                                "type": "字符串"
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
            "description": "此策略资源的示例 API Swagger 内容。"
          },
      "spec": {
            "remediationAction": "强制实施",
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
      "description": "找到有关 Swagger 的更多信息。"
    },
    "url": "http://swagger.io"
  }
