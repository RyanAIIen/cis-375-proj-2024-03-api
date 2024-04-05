from django.contrib.admin import AdminSite as DefaultAdminSite


class AdminSite(DefaultAdminSite):
    site_header = "Hotel Manager API Admin"


admin_site = AdminSite(name="hotel_manager_api")
