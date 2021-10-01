{
    "swagger": "2.0",
    "info": {
      "description": "이 문서는 IBM Multicloud Manager의 정책 리소스용입니다(policy.mcm.ibm.com).\nIBM Multicloud Manager 정책 리소스에는 네 가지 가능한 요청(작성, 모든 정책 조회, 하나의 정책 조회, 삭제)이 있습니다.",
      "version": "3.2.1",
      "title": "IBM Multicloud Manager 정책 API 문서",
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
        "description": "정책 리소스로 정책을 작성하고 관리합니다."
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
          "summary": "정책 작성",
          "description": "정책을 작성하여 클러스터 통제 및 위험성을 보고하고 유효성 검증합니다.",
          "operationId": "createPolicy",
          "consumes": [
            "application/yaml"
          ],
          "parameters": [
            {
              "in": "본문",
              "name": "본문",
              "description": "작성되는 정책을 설명하는 매개변수입니다.",
              "required": true,
              "schema": {
                "$ref": "#/definitions/Policy"
              }
            },
            {
              "in": "경로",
              "name": "네임스페이스",
              "description": "사용하려는 네임스페이스입니다(예제: 기본값).",
              "required": true,
              "type": "문자열"
            },
            {
              "name": "쿠키",
              "in": "헤더",
              "description": "권한: 전달자 {ACCESS_TOKEN}, ACCESS_TOKEN은 사용자 액세스 토큰입니다.",
              "type": "문자열",
              "required": true
            }
          ],
          "responses": {
            "200": {
              "description": "성공"
            },
            "403": {
              "description": "액세스 금지됨"
            },
            "404": {
              "description": "리소스를 찾을 수 없음"
            },
            "500": {
              "description": "내부 서비스 오류"
            },
            "503": {
              "description": "사용 불가능한 서비스"
            }
          }
        },
        "get": {
          "tags": [
            "Policy.mcm.ibm.com"
          ],
          "summary": "모든 정책 조회",
          "description": "세부사항은 정책을 조회하십시오.",
          "operationId": "queryPolicies",
          "consumes": [
            "application/yaml"
          ],
          "parameters": [
            {
              "in": "경로",
              "name": "네임스페이스",
              "description": "사용하려는 네임스페이스입니다(예제: 기본값).",
              "required": true,
              "type": "문자열"
            },
            {
              "name": "쿠키",
              "in": "헤더",
              "description": "권한: 전달자 {ACCESS_TOKEN}, ACCESS_TOKEN은 사용자 액세스 토큰입니다.",
              "type": "문자열",
              "required": true
            }
          ],
          "responses": {
            "200": {
              "description": "성공"
            },
            "403": {
              "description": "액세스 금지됨"
            },
            "404": {
              "description": "리소스를 찾을 수 없음"
            },
            "500": {
              "description": "내부 서비스 오류"
            },
            "503": {
              "description": "사용 불가능한 서비스"
            }
          }
        }
      },
      "/policy.mcm.ibm.com/v1alpha1/namespaces/{namespace}/policies/{policy_name}": {
        "get": {
          "tags": [
            "Policy.mcm.ibm.com"
          ],
          "summary": "하나의 정책 조회",
          "description": "세부사항은 하나의 정책을 조회하십시오.",
          "operationId": "queryPolicy",
          "parameters": [
            {
              "name": "policy_name",
              "in": "경로",
              "description": "조회하려는 정책의 이름입니다.",
              "required": true,
              "type": "문자열"
            },
            {
              "in": "경로",
              "name": "네임스페이스",
              "description": "사용하려는 네임스페이스입니다(예제: 기본값).",
              "required": true,
              "type": "문자열"
            },
            {
              "name": "쿠키",
              "in": "헤더",
              "description": "권한: 전달자 {ACCESS_TOKEN}, ACCESS_TOKEN은 사용자 액세스 토큰입니다.",
              "type": "문자열",
              "required": true
            }
          ],
          "responses": {
            "200": {
              "description": "성공"
            },
            "403": {
              "description": "액세스 금지됨"
            },
            "404": {
              "description": "리소스를 찾을 수 없음"
            },
            "500": {
              "description": "내부 서비스 오류"
            },
            "503": {
              "description": "사용 불가능한 서비스"
            }
          }
        },
        "delete": {
          "tags": [
            "Policy.mcm.ibm.com"
          ],
          "summary": "정책 삭제",
          "description": "",
          "operationId": "deletePolicy",
          "parameters": [
            {
              "name": "policy_name",
              "in": "경로",
              "description": "삭제하려는 정책의 이름입니다.",
              "required": true,
              "type": "문자열"
            },
            {
              "in": "경로",
              "name": "네임스페이스",
              "description": "사용하려는 네임스페이스입니다(예제: 기본값).",
              "required": true,
              "type": "문자열"
            },
            {
              "name": "쿠키",
              "in": "헤더",
              "description": "권한: 전달자 {ACCESS_TOKEN}, ACCESS_TOKEN은 사용자 액세스 토큰입니다.",
              "type": "문자열",
              "required": true
            }
          ],
          "responses": {
            "200": {
              "description": "성공"
            },
            "403": {
              "description": "액세스 금지됨"
            },
            "404": {
              "description": "리소스를 찾을 수 없음"
            },
            "500": {
              "description": "내부 서비스 오류"
            },
            "503": {
              "description": "사용 불가능한 서비스"
            }
          }
        }
      }
    },
    "definitions": {
      "Policy": {
        "type": "오브젝트",
        "required": [
          "apiVersion",
          "유형",
          "메타데이터",
          "스펙"
        ],
        "properties": {
          "apiVersion": {
            "type": "문자열"
          },
          "kind": {
            "type": "문자열"
          },
          "metadata": {
            "type": "오브젝트"
          },
          "spec": {
            "type": "오브젝트",
            "properties": {
              "remediationAction": {
                "type": "문자열"
              },
              "namespaces": {
                "type": "오브젝트",
                "properties": {
                  "include": {
                    "type": "배열",
                    "items": {
                      "type": "문자열"
                    }
                  },
                  "exclude": {
                    "type": "배열",
                    "items": {
                      "type": "문자열"
                    }
                  }
                }
              },
              "roleTemplates": {
                "type": "오브젝트",
                "properties": {
                  "kind": {
                    "type": "문자열"
                  },
                  "apiVersion": {
                    "type": "문자열"
                  },
                  "complianceType": {
                    "type": "문자열"
                  },
                  "metadata": {
                    "type": "오브젝트"
                  },
                  "selector": {
                    "type": "오브젝트",
                    "properties": {
                      "matchLabels": {
                        "type": "오브젝트"
                      }
                    }
                  },
                  "rules": {
                    "type": "배열",
                    "items": {
                      "type": "오브젝트",
                      "properties": {
                        "complianceType": {
                          "type": "문자열"
                        },
                        "PolicyRule": {
                          "type": "오브젝트",
                          "properties": {
                            "apiGroups": {
                              "type": "배열",
                              "items": {
                                "type": "문자열"
                              }
                            },
                            "resources": {
                              "type": "배열",
                              "items": {
                                "type": "문자열"
                              }
                            },
                            "verbs": {
                              "type": "배열",
                              "items": {
                                "type": "문자열"
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
          "kind": "정책",
          "metadata": {
            "name": "test-policy-swagger",
            "description": "정책 리소스의 API Swagger 컨텐츠 예제입니다."
          },
          "spec": {
            "remediationAction": "적용",
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
                "namespace": 널,
                "name": "테스트 역할"
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
                    "확장기능",
                    "앱"
                  ],
                  "resources": [
                    "배치"
                  ],
                  "verbs": [
                    "가져오기",
                    "목록",
                    "감시",
                    "삭제"
                  ]
                }
              },
              {
                "complianceType": "mustnothave",
                "PolicyRule": {
                  "apiGroups": [
                    "코어"
                  ],
                  "resources": [
                    "팟(Pod)"
                  ],
                  "verbs": [
                    "작성",
                    "업데이트",
                    "패치"
                  ]
                }
              },
              {
                "PolicyRule": 널,
                "apiGroups": [
                  "코어"
                ],
                "resources": [
                  "시크릿"
                ],
                "verbs": [
                  "가져오기",
                  "감시",
                  "목록",
                  "작성",
                  "삭제",
                  "업데이트",
                  "patchß"
                ]
              }
            ]
          }
        }
      }
    },
    "externalDocs": {
      "description": "Swagger에 대해 추가로 찾아보십시오."
    },
    "url": "http://swagger.io"
  }
