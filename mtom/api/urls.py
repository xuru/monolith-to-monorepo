from django.urls import include, path

urlpatterns = [
    path("auth/", include(("mtom.authentication.urls", "authentication"))),
    path("users/", include(("mtom.users.urls", "users"))),
    path("errors/", include(("mtom.errors.urls", "errors"))),
    path("files/", include(("mtom.files.urls", "files"))),
]
