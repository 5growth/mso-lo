*** Variables ***
${MSO-LO_HOST}      localhost    # Hostname of the MSO-LO
${MSO-LO_PORT}      80	    # Listening port of the MSO-LO
${HTTP}    http
${MSO-LO_BASE_API}  ${HTTP}://${MSO-LO_HOST}:${MSO-LO_PORT}
${SCHEMAS_PATH}     ../tests/response_schemas.py

${AUTHORIZATION}    Bearer    QWxhZGRpbjpvcGVuIHNlc2FtZQ==
${CONTENT_TYPE}    application/json
${CONTENT_TYPE_PATCH}    application/merge-patch+json
${ACCEPT_JSON}         application/json
${ACCEPT}         application/json
${apiRoot}        nfvo
${nfvoId}         1
${nfvoIdinexistent}         80
${AUTH_USAGE}     1
${WRONG_AUTHORIZATION}    Bearer    XXXXXWRONGXXXXX
${MAX_WAIT}   2 min
${INTERVAL_WAIT}    2 s
${nsdId}    pingpong
${nsInstanceId}       cc256072-2001-434c-8be9-0bd8609cef9f
${nsInstanceIdinexistent}       6fc3539c-e602-4afa-8e13-962fb5a7d81xxxxxxx
${ConflictNsInstanceId}    007c111c-e602-4afa-8e13-962fb5a7d81d
${nsInstanceName}    Test-nsInstance
${nsInstanceDescription}    description ns
${vnfInstanceIds}    []
${vimAccountIds}    ['c25ce403-b664-48e3-b790-9ed7635feffc']
${vldName}          'mgmt_vl'
${vimNetworkName}   'test'
${notificationUri}   http://192.168.18.14:8083/
${SINGLE_FILE_VNFD}    1    # If VNFD is PLAIN TEXT
${ACCEPT_PLAIN}    text/plain
${ACCEPT_ZIP}     application/zip
${nsPkgId_processing}    007c111c-38a1-42c0-a666-7475ecb1567c
${ARTIFACT_TYPE}    application/octet-stream
${ARTIFACT_ID}    artifactId
${WRONG_ACCEPT}    application/json
${nsLcmOpOccId}    6fc3539c-e602-4afa-8e13-962fb5a7d81d
${CancelMode}    GRACEFUL
${NFVO_DUPLICATION}    0
${sub_filter}    filter
${sub_filter_invalid}    filter_invalid
${fields}         criteria,objectInstanceIds

${response}    {}


${NEG_FILTER}    attribute_not_exist=some_value
${NEG_SELECTOR}    fields=wrong_field
