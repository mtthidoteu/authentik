"""SCIM URLs"""
from django.urls import path

from authentik.sources.scim.views.v2 import (
    groups,
    resource_types,
    schemas,
    service_provider_config,
    users,
)

urlpatterns = [
    path(
        "<slug:source_slug>/v2/Users",
        users.UsersView.as_view(),
        name="v2-users",
    ),
    path(
        "<slug:source_slug>/v2/Users/<str:user_id>",
        users.UsersView.as_view(),
        name="v2-users",
    ),
    path(
        "<slug:source_slug>/v2/Groups",
        groups.GroupsView.as_view(),
        name="v2-groups",
    ),
    path(
        "<slug:source_slug>/v2/Groups/<str:group_id>",
        groups.GroupsView.as_view(),
        name="v2-groups",
    ),
    path(
        "<slug:source_slug>/v2/Schemas",
        schemas.SchemaView.as_view(),
        name="v2-schema",
    ),
    path(
        "<slug:source_slug>/v2/Schemas/<str:schema_uri>",
        schemas.SchemaView.as_view(),
        name="v2-schema",
    ),
    path(
        "<slug:source_slug>/v2/ServiceProviderConfig",
        service_provider_config.ServiceProviderConfigView.as_view(),
        name="v2-service-provider-config",
    ),
    path(
        "<slug:source_slug>/v2/ResourceTypes",
        resource_types.ResourceTypesView.as_view(),
        name="v2-resource-types",
    ),
    path(
        "<slug:source_slug>/v2/ResourceTypes/<str:resource_type>",
        resource_types.ResourceTypesView.as_view(),
        name="v2-resource-types",
    ),
]
