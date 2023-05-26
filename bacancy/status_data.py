status1 = """{
            "UUID": "231960e8-14b7-49eb-a160-76cc1a78edbb",
            "StateTransitionReason": "USER_INITIATED",
            "LastModified": 1569284520.333,
            "BatchSize": 5,
            "State": "Enabled",
            "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function",
            "EventSourceArn": "arn:aws:sqs:us-west-2:123456789012:mySQSqueue"
            "test" : [
                      a: value
                        ]
            }"""

status2 = """{
            "UUID": "231960e8-14b7-49eb-a160-76cc1a78edbc",
            "StateTransitionReason": "USER_INITIATED",
            "LastModified": 1569284520.333,
            "BatchSize": 5,
            "State": "Disabled",
            "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function",
            "EventSourceArn": "arn:aws:sqs:us-west-2:123456789012:mySQSqueue"
            }"""

status3 = """{
            "UUID": "231960e8-14b7-49eb-a160-76cc1a78edbd",
            "StateTransitionReason": "USER_INITIATED",
            "LastModified": 1569284520.333,
            "BatchSize": 5,
            "State": "Disabled",
            "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function",
            "EventSourceArn": "arn:aws:sqs:us-west-2:123456789012:mySQSqueue"
            }"""
