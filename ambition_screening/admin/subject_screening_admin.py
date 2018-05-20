from django.conf import settings
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from ..admin_site import ambition_screening_admin
from ..forms import SubjectScreeningForm
from ..models import SubjectScreening
from .modeladmin_mixins import ModelAdminMixin


@admin.register(SubjectScreening, site=ambition_screening_admin)
class SubjectScreeningAdmin(ModelAdminMixin, SimpleHistoryAdmin, admin.ModelAdmin):

    form = SubjectScreeningForm

    post_url_on_delete_name = settings.DASHBOARD_URL_NAMES.get(
        'screening_dashboard_url')

    radio_fields = {
        'gender': admin.VERTICAL,
        'meningitis_dx': admin.VERTICAL,
        'will_hiv_test': admin.VERTICAL,
        'mental_status': admin.VERTICAL,
        'consent_ability': admin.VERTICAL,
        'pregnancy': admin.VERTICAL,
        'breast_feeding': admin.VERTICAL,
        'previous_drug_reaction': admin.VERTICAL,
        'contraindicated_meds': admin.VERTICAL,
        'received_amphotericin': admin.VERTICAL,
        'received_fluconazole': admin.VERTICAL,
        'unsuitable_for_study': admin.VERTICAL}

    fieldsets = (
        (None, {
            'fields': (
                'report_datetime',
                'gender',
                'age_in_years',
                'meningitis_dx',
                'will_hiv_test',
                'mental_status',
                'consent_ability',
                'pregnancy',
                'preg_test_date',
                'breast_feeding',
                'previous_drug_reaction',
                'contraindicated_meds',
                'received_amphotericin',
                'received_fluconazole',
                'unsuitable_for_study',
                'reasons_unsuitable',)
        }),
        ('Blood Results', {
            'fields': (
                'alt',
                'neutrophil',
                'platelets')
        }),
    )
