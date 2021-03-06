# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .tracked_resource_py3 import TrackedResource


class Topic(TrackedResource):
    """EventGrid Topic.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified identifier of the resource
    :vartype id: str
    :ivar name: Name of the resource
    :vartype name: str
    :ivar type: Type of the resource
    :vartype type: str
    :param location: Required. Location of the resource
    :type location: str
    :param tags: Tags of the resource
    :type tags: dict[str, str]
    :ivar provisioning_state: Provisioning state of the topic. Possible values
     include: 'Creating', 'Updating', 'Deleting', 'Succeeded', 'Canceled',
     'Failed'
    :vartype provisioning_state: str or
     ~microsoft.azure.management.eventgrid.models.TopicProvisioningState
    :ivar endpoint: Endpoint for the topic.
    :vartype endpoint: str
    :param input_schema: This determines the format that Event Grid should
     expect for incoming events published to the topic. Possible values
     include: 'EventGridSchema', 'CustomEventSchema', 'CloudEventSchemaV1_0'.
     Default value: "EventGridSchema" .
    :type input_schema: str or
     ~microsoft.azure.management.eventgrid.models.InputSchema
    :param input_schema_mapping: This enables publishing using custom event
     schemas. An InputSchemaMapping can be specified to map various properties
     of a source schema to various required properties of the EventGridEvent
     schema.
    :type input_schema_mapping:
     ~microsoft.azure.management.eventgrid.models.InputSchemaMapping
    :ivar metric_resource_id: Metric resource id for the topic.
    :vartype metric_resource_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'endpoint': {'readonly': True},
        'metric_resource_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'endpoint': {'key': 'properties.endpoint', 'type': 'str'},
        'input_schema': {'key': 'properties.inputSchema', 'type': 'str'},
        'input_schema_mapping': {'key': 'properties.inputSchemaMapping', 'type': 'InputSchemaMapping'},
        'metric_resource_id': {'key': 'properties.metricResourceId', 'type': 'str'},
    }

    def __init__(self, *, location: str, tags=None, input_schema="EventGridSchema", input_schema_mapping=None, **kwargs) -> None:
        super(Topic, self).__init__(location=location, tags=tags, **kwargs)
        self.provisioning_state = None
        self.endpoint = None
        self.input_schema = input_schema
        self.input_schema_mapping = input_schema_mapping
        self.metric_resource_id = None
