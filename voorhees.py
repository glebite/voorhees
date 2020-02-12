import json

class Voorhees:
    def __init__(self,json_string):
        self.incoming_json_string = json_string
        
    def abyss_copy(self, key):
        acc_result = ""
        def walk(obj, acc_result, key):
            """Recursively search for values of key in JSON tree."""
            if isinstance(obj, dict):
                acc_result += '{'
                for k, v in obj.items():
                    if k == key:
                        k = key+'changed'
                    if isinstance(v, (dict, list)):
                        acc_result += '"' + k + '":'                    
                        acc_result = walk(v, acc_result, key)
                    else:
                        acc_result += '"' + k + '":'                                        
                        if type(v) == str:
                            acc_result += '"{}",'.format(v)
                        elif type(v) == int:
                            acc_result += '{},'.format(v)
                        elif type(v) == bool:
                            acc_result += '{},'.format(v)                    
                acc_result = acc_result[:-1]; acc_result += '},'
            elif isinstance(obj, list):
                acc_result += '['
                for item in obj:
                    acc_result = walk(item, acc_result, key)
                acc_result = acc_result[:-1]; acc_result += '],'
            else:
                if type(obj) == str:
                    acc_result += "'" + str(obj) +'"'; acc_result += ","
                elif type(obj) == int:
                    acc_result += str(obj); acc_result += ","
            return acc_result
        acc_result = walk(self.incoming_json_string, acc_result, key)
        return acc_result[:-1]

data = json.loads('{"data": [{"accessProfile": {"creationTime": "2020-02-11T16:30:24.765Z", "description": "Can view dashboards, locations and services", "id": "f0a41255-0d95-03bf-a37f-b1b23d456789", "label": "viewableLabel", "lastUpdateTime": "2020-02-11T16:30:24.765Z", "permissions": "TENANT_ADMIN, SUPER_USER", "profileName": "Subscriber - Service Assurance", "tenantId": "f0a41255-0d95-03bf-a37f-b1b23d456789", "tenantType": "Subscriber", "type": "ACCESS_PROFILE"}, "address": {"addressLine1": "123 Street", "addressLine2": "301 Front St W", "addressLine3": "Riverside", "city": "Toronto", "country": "Canada", "otherAddressDetails": "Next to the Roundhouse Park", "pin": "111 123", "province": "Ontario"}, "contact": {"email": "john.smith@example.com", "name": "John Smith"}, "creationTime": "2020-02-11T16:30:24.765Z", "emailProperties": {"fromDisplayName": "No Reply", "fromEmail": "no_reply@company.com", "replyEmail": "contactUs@company.com"}, "id": "f0a41255-0d95-03bf-a37f-b1b23d456789", "label": "viewableLabel", "lastUpdateTime": "2020-02-11T16:30:24.765Z", "parentTenant": {"id": "f0a41255-0d95-03bf-a37f-b1b23d456789", "label": "viewableLabel", "subTenantId": "subTenantId", "tenantId": "parentTenantId"}, "serviceLocations": [{"id": "f0a41255-0d95-03bf-a37f-b1b23d456789", "label": "viewableLabel", "subTenantId": "subTenantId", "tenantId": "parentTenantId"}], "tenantId": "f0a41255-0d95-03bf-a37f-b1b23d456789", "tenantState": "ACTIVE", "tenantType": "RESELLER", "type": "ACCESS_PROFILE", "workflowPolicy": {"automatedFulfillment": true, "manuallyReviewed": false}}], "error": {"affectedEntities": ["f0a41255-0d95-03bf-a37f-b1b23d456789", "f0a41255-0d95-03bf-a37f-b1b23d456789"], "info": "Entity not found", "type": "NOT_FOUND"}}')

x = Voorhees(data)
print(x.abyss_copy('contact'))
