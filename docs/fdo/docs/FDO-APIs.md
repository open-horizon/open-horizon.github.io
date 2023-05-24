---
copyright:
years: 2022 - 2023
lastupdated: "2023-05-24"
title: "FDO API guide"
description: "FDO API detailed documentation"

parent: FDO Protocol Reference
nav_order: 1
grand_parent: Administering
---

# FDO API documentation

This page describes the FIDO Device Onboard (FDO) REST API interfaces.

## FDO Owner Services API

***NOTE***: These REST APIs use Digest authentication. `api_user` and `api_password` properties specify the credentials to be used while making the REST calls. The value for `api_user` is present in `service.yml` file and value for `api_password` is present in `service.env` file.

| Operation                      | Description                        | Path/Query Parameters    | Content Type   |Request Body  | Response Body | Sample cURL call |
| ------------------------------:|:----------------------------------:|:------------------------:|:--------------:|-------------:|--------------:|-----------------:|
| POST /api/v1/owner/redirect    | Updates TO2 RVBlob in `ONBOARDING_CONFIG` table. | | text/plain | RVTO2Addr in diagnostic form | | curl -D - --digest -u ${api_user}: --location --request POST 'http://localhost:8042/api/v1/owner/redirect' --header 'Content-Type: text/plain'  --data-raw '[["localhost","127.0.0.1",8042,3]]' |
| GET /api/v1/to0/{guid} | initiate TO0 from Owner | GUID of the device to initiate TO0 |  |  |  | curl  -D - --digest -u ${api_user}: --location --request GET "http://localhost:8042/api/v1/to0/${device_guid}" --header 'Content-Type: text/plain' |
| POST /api/v1/owner/svi | Uploads SVI instructions to `SYSTEM_PACKAGE` table. |  | text/plain | SVI Instruction |   | curl -D - --digest -u ${api_user}: --location --request POST 'http://localhost:8042/api/v1/owner/svi' --header 'Content-Type: text/plain' --data-raw '[{"filedesc" : "setup.sh","resource" : "URL"}, {"exec" : ["bash","setup.sh"] }]' |
| GET /api/v1/owner/vouchers | Returns a list of all Ownership Voucher GUIDs. | | | | line separated list of GUIDs | curl  -D - --digest -u ${api_user}: --location --request GET "http://localhost:8042/api/v1/owner/vouchers" --header 'Content-Type: text/plain' |
| GET /api/v1/owner/vouchers/<device_guid> | Returns the Ownership Voucher for the specified GUID. | Path - id: Device GUID | | | Ownership Voucher | curl  -D - --digest -u ${api_user}: --location --request GET "http://localhost:8042/api/v1/owner/vouchers/${device_guid}" --header 'Content-Type: text/plain' |
| POST /api/v1/owner/vouchers/ | Insert Ownership Voucher against the specified GUID in `ONBOARDING_VOUCHER` table. | | text/plain | Content of Ownership Voucher in PEM Format | Guid of the device |  curl  -D - --digest -u ${api_user}: --location --request POST "http://localhost:8042/api/v1/owner/vouchers" --header 'Content-Type: text/plain' --data-raw '${voucher}' |
| GET /api/v1/logs | Serves the log from the owner service | | | | owner logs| curl  -D - --digest -u ${api_user}:  --location --request GET 'http://localhost:8042/api/v1/logs' |
| DELETE /api/v1/logs | Deletes the log from the owner service | | |  | | curl  -D - --digest -u ${api_user}:  --location --request DELETE 'http://localhost:8042/api/v1/logs' |
| GET /health | Returns the health status |  |  | | Current version |  curl  -D - --digest -u ${api_user}:  --location --request GET 'http://localhost:8042/health'|
| GET /api/v1/ondie | Serves the stored certs & crls files | | | | Ondie certs & crl files | curl  -D - --digest -u ${api_user}:  --location --request GET 'http://localhost:8042/api/v1/ondie' |
| POST /api/v1/ondie | To insert onDie certs and crls zip file to DB | | text/plain | Path to ondie cert file | |  curl -D - --digest -u ${api_user}:${api_passwd} --location --request POST "http://${ip}:{port}/api/v1/ondie" --header 'Content-Type: text/plain' --data-raw "${cert-file}" |
| GET /api/v1/certificate?filename=fileName | Returns the certificate file based on filename | Query - filename | | | Certificate file in PKCS12 format | curl  -D - --digest -u ${api_user}: --location --request GET 'http://localhost:8042/api/v1/certificate?filename=ssl.p12' |
| GET /api/v1/certificate?alias={alias} | Returns the owner certificate of the given alias type | Query - alias | | | Certificate PEM format | curl  -D - --digest -u ${api_user}: --location --request GET 'http://localhost:8042/api/v1/certificate?alias=SECP256R1' --header 'Content-Type: text/plain' |
| GET /api/v1/certificate?uuid=uuid | Returns the owner alias type for the given voucher| Query - uuid | | |  UUID's attestation type | curl  -D - --digest -u ${api_user}: --location --request GET 'http://localhost:8042/api/v1/certificate?uuid=cc60f0aa-56d0-492e-8c8d-9a1fe55cb60 --header 'Content-Type: text/plain' |
| POST /api/v1/certificate?filename=fileName | Adds the certificate file to DB based on filename | Query - filename | text/plain | PKCS12 Certificate file in Binary format |  | curl -D - --digest -u ${api_user}: --location --request POST 'http://localhost:8042/api/v1/certificate?filename=ssl.p12' --header 'Content-Type: text/plain' --data-binary '@< path to ssl.p12 >' |
| DELETE /api/v1/certificate?filename=fileName | Delete the certificate file to DB based on filename | Query - filename | | |  | curl  -D - --digest -u ${api_user}: --location --request DELETE 'http://localhost:8042/api/v1/certificate?filename=ssl.p12' --header 'Content-Type: text/plain' |
| POST /api/v1/certificate/validity?days=no_of_days | Updates certificate validity in `CERTIFICATE_VALIDITY` table | | text/plain |  | | curl  -D - --digest -u ${api_user}: --location --request POST 'http://localhost:8042/api/v1/certificate/validity?days=10'  --header 'Content-Type: text/plain' |
| GET /api/v1/certificate/validity | Collects certificate validity days from  `CERTIFICATE_VALIDITY` table | |  | | Number of Days| curl  -D - --digest -u ${api_user}: --location --request GET 'http://localhost:8042/api/v1/certificate/validity' |
| GET /api/v1/owner/messagesize | Collects the max message size from `ONBOARDING_CONFIG` table | | |  | MAX_MESSAGE_SIZE | curl -D - --digest -u ${api_user}: --location --request GET 'http://localhost:8042/api/v1/owner/messagesize' --header 'Content-Type: text/plain'|
| POST /api/v1/owner/messagesize | Updates the max message size in `ONBOARDING_CONFIG` table | | text/plain | MAX_MESSAGE_SIZE | | curl -D - --digest -u ${api_user}: --location --request POST 'http://localhost:8042/api/v1/owner/messagesize' --header 'Content-Type: text/plain' --data-raw '10000'|
| GET /api/v1/owner/svisize | Collects the owner svi size from `ONBOARDING_CONFIG` table | |  |  | SVI_MESSAGE_SIZE | curl -D - --digest -u ${api_user}: --location --request GET 'http://localhost:8042/api/v1/owner/svisize' --header 'Content-Type: text/plain' |
| POST /api/v1/owner/svisize | Updates the owner svi size in `ONBOARDING_CONFIG` table | | text/plain | SVI_MESSAGE_SIZE | | curl -D - --digest -u ${api_user}: --location --request POST 'http://localhost:8042/api/v1/owner/svisize' --header 'Content-Type: text/plain' --data-raw '10000' |
| GET /api/v1/owner/resource?filename=fileName | Returns the file based on filename from `SYSTEM_RESOURCE` table | Query - filename | | | file content |  curl -D - --digest -u ${api_user}: --location --request GET 'http://localhost:8042/api/v1/owner/resource?filename=fileName' --header 'Content-Type: text/plain'  |
| POST /api/v1/owner/resource?filename=fileName | Adds the file to DB based on filename  from `SYSTEM_RESOURCE` table  | Query - filename | text/plain | file in Binary format |  |  curl -D - --digest -u ${api_user}: --location --request POST 'http://localhost:8042/api/v1/owner/resource?filename=fileName' --header 'Content-Type: text/plain' --data-binary '@< path to file >' |
| DELETE /api/v1/owner/resource?filename=fileName | Delete the  file from DB based on filename from `SYSTEM_RESOURCE` table   | Query - filename | | |  |  curl -D - --digest -u ${api_user}: --location --request DELETE 'http://localhost:8042/api/v1/owner/resource?filename=fileName' --header 'Content-Type: text/plain'|
| POST /api/v1/resell/{guid} | Gets extended resell Ownership Voucher with the guid. | Path - guid of the device to resell | | Owner Certificate | The Ownership voucher in PEM format |   curl -D - --digest -u ${api_user}: --location --request POST "http://localhost:8039/api/v1/resell/${guid}" --header 'Content-Type: text/plain' --data-raw  "$owner_certificate" -o ${serial_no}_voucher.txt |
| GET /api/v1/owner/state/{guid} | Returns the TO status the associated GUID | GUID of the device |  |  | Returns TO2 completed status & TO0 expiry (timestamps) |  curl  -D - --digest -u ${api_user}:  --location --request GET 'http://localhost:8042/api/v1/owner/state/{guid}' |
{: caption="Table 1. FDO Owner Services API" caption-side="top"}

Following is the list of REST response error codes and it's possible causes :

|     Error Code     |             Possible Causes               |
| -------------------:|:----------------------------------------:|
| `401 Unauthorized`  | When an invalid Authentication header is present with the REST Request. Make sure to use the correct REST credentials. |
| `404 Not Found`     | When an invalid REST request is sent to Owner. Make sure to use the correct REST API endpoint. |
| `405 Method Not Allowed` | When an unsupported REST method is requested. Currently, Owner supports GET, POST and DELETE only. |
| `406 Not Acceptable` | When an invalid filename is passed through the REST endpoints. |
| `500 Internal Server Error` | Due to internal error, Owner unable to fetch/copy/delete the requested file. |
{: caption="Table 2. FDO Owner Services API response error codes" caption-side="top"}

## FDO PRI Rendezvous REST APIs

***NOTE***: These REST APIs use Digest authentication. `api_user` and `api_password` properties specify the credentials to be used while making the REST calls.


| Operation                      | Description                        | Path/Query Parameters    | Content Type   |Request Body  | Response Body | Sample cURL call |
| ------------------------------:|:----------------------------------:|:------------------------:|:--------------:|-------------:|--------------:|-----------------:|
| GET /api/v1/certificate?filename=fileName | Returns the certificate file based on filename | Query - filename | | | Certificate file in PKCS12 format | curl  -D - --digest -u ${api_user}: --location --request GET 'http://localhost:8040/api/v1/certificate?filename=ssl.p12' |
| POST /api/v1/certificate?filename=fileName | Adds the certificate file to DB based on filename | Query - filename | text/plain| PKCS12 Certificate file in Binary format |  | curl -D - --digest -u ${api_user}: --location --request POST 'http://localhost:8040/api/v1/certificate?filename=ssl.p12' --data-binary '@< path to ssl.p12 >' |
| DELETE /api/v1/certificate?filename=fileName | Delete the certificate file to DB based on filename | Query - filename | | |  | curl  -D - --digest -u ${api_user}: --location --request DELETE 'http://localhost:8040/api/v1/certificate?filename=ssl.p12' --header 'Content-Type: text/plain' |
| GET /api/v1/logs | Serves the log from the RV service | | | | RV logs| curl  -D - --digest -u ${api_user}:  --location --request GET 'http://localhost:8040/api/v1/logs' |
| DELETE /api/v1/logs | Deletes the log from the RV service | | |  | | curl  -D - --digest -u ${api_user}:  --location --request DELETE 'http://localhost:8040/api/v1/logs' |
| POST /api/v1/certificate/validity?days=no_of_days | Updates certificate validity in `CERTIFICATE_VALIDITY` table | | text/plain|  | | curl  -D - --digest -u ${api_user}: --location --request POST 'http://localhost:8040/api/v1/certificate/validity?days=10' |
| GET /api/v1/certificate/validity | Collects certificate validity days from  `CERTIFICATE_VALIDITY` table | |  | | Number of Days| curl  -D - --digest -u ${api_user}: --location --request GET 'http://localhost:8040/api/v1/certificate/validity' |
| GET /health | Returns the health status |  |  | | Current version |  curl  -D - --digest -u ${api_user}:  --location --request GET 'http://localhost:8040/health'|
| POST /api/v1/rv/allow | Adds public key to allowed list of Owners in RV |  |  text/plain |  certificate in pem format | |   curl  -D - --digest -u ${api_user}:  --location --request POST 'http://localhost:8040/api/v1/rv/allow` --data-raw  "$owner_certificate" |
| DELETE /api/v1/rv/allow | delete public key to allowed list of Owners in RV |  |  text/plain |  certificate in pem format | |   curl  -D - --digest -u ${api_user}:  --location --request POST 'http://localhost:8040/api/v1/rv/allow` --data-raw  "$owner_certificate" |
| POST /api/v1/rv/deny | Adds public key to denied list of Owners in RV |  |  text/plain |  certificate in pem format | |   curl  -D - --digest -u ${api_user}:  --location --request POST 'http://localhost:8040/api/v1/rv/deny` --data-raw  "$owner_certificate" |
{: caption="Table 3. FDO PRI Rendezvous API" caption-side="top"}

Following is the list of REST response error codes and it's description :

|     Error Code     |             Possible Causes               |
| -------------------:|:----------------------------------------:|
| `401 Unauthorized`  | When an invalid Authentication header is present with the REST Request. Make sure to use the correct REST credentials. |
| `404 Not Found`     | When an invalid REST request is sent to RV. Make sure to use the correct REST API endpoint. |
| `405 Method Not Allowed` | When an unsupported REST method is requested. Currently, RV supports GET, PUT and DELETE only. |
| `406 Not Acceptable` | When an invalid filename is passed through the REST endpoints. |
| `500 Internal Server Error` | Due to internal error, RV unable to fetch/copy/delete the requested file. |
{: caption="Table 4. FDO PRI Rendezvous API response error codes" caption-side="top"}

## FDO PRI Manufacturer REST APIs

***NOTE***: These REST APIs use Digest authentication. `api_user` and `api_password` properties specify the credentials to be used while making the REST calls. The value for `api_user` is present in `service.yml` file and value for `api_password` is present in `service.env` file.

| Operation                      | Description                        | Path/Query Parameters    | Content Type   |Request Body  | Response Body | Sample cURL call |
| ------------------------------:|:----------------------------------:|:------------------------:|:--------------:|-------------:|--------------:|-----------------:|
| POST /api/v1/mfg/vouchers/<serial_no> | Gets extended Ownership Voucher with the serial number. | Path - Device Serial Number | | Owner Certificate | Extended Voucher |   curl -D - --digest -u ${api_user}: --location --request POST "http://localhost:8039/api/v1/mfg/vouchers/${serial_no}" --header 'Content-Type: text/plain' --data-raw  "$owner_certificate" -o ${serial_no}_voucher.txt |
| GET /api/v1/certificate?filename=fileName | Returns the certificate file based on filename | Query - filename | |  | Keystore file in binary format | curl  -D - --digest -u ${api_user}: --location --request GET 'http://localhost:8039/api/v1/certificate?filename=ssl.p12' |
| POST /api/v1/certificate?filename=fileName | Adds the certificate file to DB based on filename | Query - filename | text/plain| PKCS12 Certificate file in Binary format |  | curl -D - --digest -u ${api_user}: --location --request POST 'http://localhost:8039/api/v1/certificate?filename=ssl.p12' --header 'Content-Type: text/plain' --data-binary '@< path to ssl.p12 >' |
| DELETE /api/v1/certificate?filename=fileName | Delete the certificate file to DB based on filename | Query - filename | | |  | curl  -D - --digest -u ${api_user}: --location --request DELETE 'http://localhost:8039/api/v1/certificate?filename=ssl.p12' --header 'Content-Type: text/plain' |
| POST /api/v1/rvinfo/ | Updates RV Info in `RV_DATA` table | | text/plain | RV Info |   |  curl  -D - --digest -u ${api_user}: --location --request POST 'http://localhost:8039/api/v1/rvinfo' --header 'Content-Type: text/plain' --data-raw '[[[5,"localhost"],[3,8040],[12,1],[2,"127.0.0.1"],[4,8041]]]' |
| GET /api/v1/deviceinfo/{seconds} | Serves the serial no. and GUID of the devices that completed DI in the last `n` seconds | Path - `n` seconds |  |  | JSON array of Serial No, GUID ,DI Timestamp and Attestion type. | curl -D - --digest -u apiUser:  --location --request GET 'http://localhost:8080/api/v1/deviceinfo/30' --header 'Content-Type: text/plain' |
| GET /api/v1/logs | Serves the log from the manufacturer service | | | | Manufacturer logs| curl  -D - --digest -u ${api_user}:  --location --request GET 'http://localhost:8039/api/v1/logs' --header 'Content-Type: text/plain'|
| DELETE /api/v1/logs | Deletes the log from the manufacturer service | | |  | | curl  -D - --digest -u ${api_user}:  --location --request DELETE 'http://localhost:8039/api/v1/logs' --header 'Content-Type: text/plain'|
| POST /api/v1/certificate/validity?days=no_of_days | Updates certificate validity in `CERTIFICATE_VALIDITY` table | Query - days | text/plain |  | | curl  -D - --digest -u ${api_user}: --location --request POST 'http://localhost:8039/api/v1/certificate/validity?days=10' --header 'Content-Type: text/plain' |
| GET /api/v1/certificate/validity | Collects certificate validity days from  `CERTIFICATE_VALIDITY` table | |  | | Number of Days| curl  -D - --digest -u ${api_user}: --location --request GET 'http://localhost:8039/api/v1/certificate/validity' |
| GET /health | Returns the health status |  |  | | Current version |  curl  -D - --digest -u ${api_user}:  --location --request GET 'http://localhost:8039/health' |
{: caption="Table 5. FDO PRI Manufacturer API" caption-side="top"}

Following is the list of REST response error codes and it's possible causes :

|     Error Code     |             Possible Causes               |
| -------------------:|:----------------------------------------:|
| `401 Unauthorized`  | When an invalid Authentication header is present with the REST Request. Make sure to use the correct REST credentials. |
| `404 Not Found`     | When an invalid REST request is sent to MFG. Make sure to use the correct REST API endpoint. |
| `405 Method Not Allowed` | When an unsupported REST method is requested. Currently, MFG supports GET, POST and DELETE only. |
| `406 Not Acceptable` | When an invalid filename is passed through the REST endpoints. |
| `500 Internal Server Error` | Due to internal error, MFG unable to fetch/copy/delete the requested file. |
{: caption="Table 6. FDO PRI Rendezvous API" caption-side="top"}

## FDO PRI Reseller REST APIs

| Operation                      | Description                        | Path/Query Parameters    | Content Type   |Request Body  | Response Body | Sample cURL call |
| ------------------------------:|:----------------------------------:|:------------------------:|:--------------:|-------------:|--------------:|-----------------:|
| POST /api/v1/resell/{guid} | Gets extended resell Ownership Voucher with the guid. | Path - guid of the device to resell | | Owner Certificate | The Ownership voucher in PEM format |   curl -D - --digest -u ${api_user}: --location --request POST "http://localhost:8070/api/v1/resell/${guid}" --header 'Content-Type: text/plain' --data-raw  "$owner_certificate" -o ${serial_no}_voucher.txt |
| GET /api/v1/owner/vouchers | Returns a list of all Ownership Voucher GUIDs. | | | | line separated list of GUIDs | curl  -D - --digest -u ${api_user}: --location --request GET "http://localhost:8070/api/v1/owner/vouchers" --header 'Content-Type: text/plain' |
| GET /api/v1/owner/vouchers/<device_guid> | Returns the Ownership Voucher for the specified GUID. | Query - id: Device GUID | | | Ownership Voucher | curl  -D - --digest -u ${api_user}: --location --request GET "http://localhost:8070/api/v1/owner/vouchers/${device_guid}" --header 'Content-Type: text/plain' |
| POST /api/v1/owner/vouchers/ | Insert Ownership Voucher against the specified GUID in `ONBOARDING_VOUCHER` table. | | text/plain | Content of Ownership Voucher in PEM Format | |  curl  -D - --digest -u ${api_user}: --location --request POST "http://localhost:8070/api/v1/owner/vouchers" --header 'Content-Type: text/plain' --data-binary '${voucher}' |
{: caption="Table 7. FDO PRI Reseller API" caption-side="top"}

Following is the list of REST response error codes and it's possible causes :

|     Error Code     |             Possible Causes               |
| -------------------:|:----------------------------------------:|
| `401 Unauthorized`  | When an invalid Authentication header is present with the REST Request. Make sure to use the correct REST credentials. |
| `404 Not Found`     | When an invalid REST request is sent to Reseller. Make sure to use the correct REST API endpoint. |
| `405 Method Not Allowed` | When an unsupported REST method is requested. Currently, Reseller supports GET, POST and DELETE only. |
| `406 Not Acceptable` | When an invalid filename is passed through the REST endpoints. |
| `500 Internal Server Error` | Due to internal error, Reseller unable to fetch/copy/delete the requested file. |
{: caption="Table 8. FDO PRI Reseller API response error codes" caption-side="top"}