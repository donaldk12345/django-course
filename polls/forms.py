from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient_name', 'patient_email', 'patient_phone', 'preferred_date', 'reason']
        widgets = {
            'doctor': forms.Select(attrs={
                'class': 'w-full bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl px-4 py-3 text-sm text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-sky-500'
            }),
            'patient_name': forms.TextInput(attrs={
                'class': 'w-full bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl px-4 py-3 text-sm text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-sky-500',
                'placeholder': 'Ex: Jean Dupont'
            }),
            'patient_phone': forms.TextInput(attrs={
                'class': 'w-full bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl px-4 py-3 text-sm text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-sky-500',
                'placeholder': '+237 6...'
            }),
            'patient_email': forms.EmailInput(attrs={
                'class': 'w-full bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl px-4 py-3 text-sm text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-sky-500',
                'placeholder': 'exemple@email.com'
            }),
            'preferred_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'w-full bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl px-4 py-3 text-sm text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-sky-500'
            }),
            'reason': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl px-4 py-3 text-sm text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-sky-500',
                'placeholder': 'Décrivez brièvement le motif de votre consultation...'
            }),
        }