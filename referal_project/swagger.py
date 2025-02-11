from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Referral API",
      default_version='v1',
      description="Test project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="tigrangri37@gmail.com"),
      license=openapi.License(name="Tigran official License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny]
)


class CustomAutoSchema(SwaggerAutoSchema):

   def get_tags(self, operation_keys=None):

      tags = self.overrides.get('tags', None) or getattr(self.view, 'my_tags', [])
      if not tags:
         tags = [self.view.__module__.split('.')[0]]

      return tags