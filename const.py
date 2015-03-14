CHECK_DEPLOY_STATUS = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">\
<soap:Header><SessionHeader xmlns=\"http://soap.sforce.com/2006/04/metadata\">
<sessionId>{session_id}</sessionId></SessionHeader></soap:Header><soap:Body>
<checkDeployStatus xmlns=\"http://soap.sforce.com/2006/04/metadata\">
<ID>{id}</ID>
<includeDetails>true</includeDetails>
</checkDeployStatus>
</soap:Body></soap:Envelope>
"""

DEPLOY_BODY = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"
xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<soap:Header><SessionHeader xmlns=\"http://soap.sforce.com/2006/04/metadata\">
<sessionId>{session_id}</sessionId></SessionHeader></soap:Header><soap:Body>
<deploy xmlns=\"http://soap.sforce.com/2006/04/metadata\">
<ZipFile>{zipfile}</ZipFile>
<DeployOptions>
<allowMissingFiles>false</allowMissingFiles>
<autoUpdatePackage>false</autoUpdatePackage>
<checkOnly>{checkonly}</checkOnly>
<ignoreWarnings>false</ignoreWarnings>
<performRetrieve>false</performRetrieve>
<purgeOnDelete>false</purgeOnDelete>
<rollbackOnError>false</rollbackOnError>
<runAllTests>false</runAllTests>
<singlePackage>false</singlePackage>
</DeployOptions>
</deploy>
</soap:Body></soap:Envelope>
"""

LOGIN_BODY = """<?xml version="1.0" encoding="utf-8"?>
<env:Envelope xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:env="http://schemas.xmlsoap.org/soap/envelope/">
<env:Body>
<n1:login xmlns:n1="urn:partner.soap.sforce.com">
<n1:username>{username}</n1:username>
<n1:password>{password}</n1:password>
</n1:login>
</env:Body>
</env:Envelope>
"""

SOAP_HEADER = {
    "Content-Type":"text/xml;charset=UTF-8",
    "SOAPAction":"\"\""
}
