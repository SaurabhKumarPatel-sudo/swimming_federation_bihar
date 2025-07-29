from django.contrib import admin
from .models import Profile, Event, Record, Contact
from django.utils.html import format_html

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'photograph_preview', 'id_proof_link', 'dob_proof_link', 'address_proof_link', 'coaching_certificate_link')
    readonly_fields = ('photograph_preview', 'id_proof_link', 'dob_proof_link', 'address_proof_link', 'coaching_certificate_link')

    def photograph_preview(self, obj):
        if obj.photograph:
            return format_html('<img src="{}" width="80" height="80" style="object-fit:cover;" />', obj.photograph.url)
        return "No Image"
    photograph_preview.short_description = 'Photograph'

    def id_proof_link(self, obj):
        if obj.id_proof:
            return format_html('<a href="{}" target="_blank">View</a>', obj.id_proof.url)
        return "No File"
    id_proof_link.short_description = 'ID Proof'

    def dob_proof_link(self, obj):
        if obj.dob_proof:
            return format_html('<a href="{}" target="_blank">View</a>', obj.dob_proof.url)
        return "No File"
    dob_proof_link.short_description = 'DOB Proof'

    def address_proof_link(self, obj):
        if obj.address_proof:
            return format_html('<a href="{}" target="_blank">View</a>', obj.address_proof.url)
        return "No File"
    address_proof_link.short_description = 'Address Proof'

    def coaching_certificate_link(self, obj):
        if obj.coaching_certificate:
            return format_html('<a href="{}" target="_blank">View</a>', obj.coaching_certificate.url)
        return "No File"
    coaching_certificate_link.short_description = 'Coaching Certificate'

admin.site.register(Event)
admin.site.register(Record)
admin.site.register(Contact)
