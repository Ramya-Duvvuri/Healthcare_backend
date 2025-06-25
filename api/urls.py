from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView,
    PatientListCreateView, PatientDetailView,
    DoctorListCreateView, DoctorDetailView,
    PatientDoctorMappingListCreateView,
    PatientDoctorMappingByPatientView,
    PatientDoctorMappingDeleteView
)

urlpatterns = [
    # Auth
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Patient
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),

    # Doctor
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),

    # Mappings
   path('mappings/', PatientDoctorMappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<patient_id>/', PatientDoctorMappingByPatientView.as_view(), name='mapping-by-patient'),
    path('mappings/delete/<int:pk>/', PatientDoctorMappingDeleteView.as_view(), name='mapping-delete'),
]
