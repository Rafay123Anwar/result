# # # from django.contrib import admin
# # # from .models import Result

# # # admin.site.register(Result)


# # from django.urls import path
# # from django.shortcuts import render, redirect
# # from django.contrib import admin
# # from django.http import HttpResponseRedirect
# # import csv
# # from .models import Result

# # class ResultAdmin(admin.ModelAdmin):
# #     list_display = ('roll_no', 'linear_algebra', 'oop_theory', 'oop_practical',
# #                     'pakistan_studies', 'islamic_studies', 'digital_logic_theory', 
# #                     'digital_logic_practical', 'communication_skills')

# #     def get_urls(self):
# #         # Custom URL for Upload CSV
# #         urls = super().get_urls()
# #         custom_urls = [
# #             path('upload-csv/', self.upload_csv, name="upload_csv"),
# #         ]
# #         return custom_urls + urls

# #     def upload_csv(self, request):
# #         # Render the upload form
# #         if request.method == "POST":
# #             csv_file = request.FILES.get("csv_file")
# #             if not csv_file.name.endswith('.csv'):
# #                 self.message_user(request, "This is not a valid CSV file.", level='error')
# #                 return HttpResponseRedirect(request.path)

# #             # Read and process CSV data
# #             file_data = csv_file.read().decode("utf-8").splitlines()
# #             reader = csv.DictReader(file_data)
# #             for row in reader:
# #                 Result.objects.update_or_create(
# #                     roll_no=row['roll_no'],
# #                     defaults={
# #                         'linear_algebra': row['linear_algebra'],
# #                         'oop_theory': row['oop_theory'],
# #                         'oop_practical': row['oop_practical'],
# #                         'pakistan_studies': row['pakistan_studies'],
# #                         'islamic_studies': row['islamic_studies'],
# #                         'digital_logic_theory': row['digital_logic_theory'],
# #                         'digital_logic_practical': row['digital_logic_practical'],
# #                         'communication_skills': row['communication_skills'],
# #                     }
# #                 )
# #             self.message_user(request, "CSV file uploaded successfully.")
# #             return HttpResponseRedirect("../")  # Redirect to model admin page

# #         return render(request, "admin/upload_csv.html", {'title': "Upload CSV"})

# # admin.site.register(Result, ResultAdmin)


# from django.urls import path
# from django.shortcuts import render, redirect
# from django.contrib import admin
# from django.http import HttpResponseRedirect
# import csv
# from .models import Result

# class ResultAdmin(admin.ModelAdmin):
#     list_display = (
#         'roll_no', 'linear_algebra', 'oop_theory', 'oop_practical',
#         'pakistan_studies', 'islamic_studies', 'digital_logic_theory',
#         'digital_logic_practical', 'communication_skills'
#     )

#     def get_urls(self):
#         # Custom URL for Upload CSV
#         urls = super().get_urls()
#         custom_urls = [
#             path('upload-csv/', self.upload_csv, name="upload_csv"),
#         ]
#         return custom_urls + urls

#     def upload_csv(self, request):
#         # Handle the CSV upload form
#         if request.method == "POST":
#             csv_file = request.FILES.get("csv_file")
#             if not csv_file.name.endswith('.csv'):
#                 self.message_user(request, "This is not a valid CSV file.", level='error')
#                 return HttpResponseRedirect(request.path)

#             # Process the CSV data
#             file_data = csv_file.read().decode("utf-8").splitlines()
#             reader = csv.DictReader(file_data)
#             for row in reader:
#                 Result.objects.update_or_create(
#                     roll_no=row['roll_no'],
#                     defaults={
#                         'linear_algebra': row['linear_algebra'],
#                         'oop_theory': row['oop_theory'],
#                         'oop_practical': row['oop_practical'],
#                         'pakistan_studies': row['pakistan_studies'],
#                         'islamic_studies': row['islamic_studies'],
#                         'digital_logic_theory': row['digital_logic_theory'],
#                         'digital_logic_practical': row['digital_logic_practical'],
#                         'communication_skills': row['communication_skills'],
#                     }
#                 )
#             self.message_user(request, "CSV file uploaded successfully.")
#             return HttpResponseRedirect("../")  # Redirect back to the admin page

#         return render(request, "admin/upload_csv.html", {'title': "Upload CSV"})

# admin.site.register(Result, ResultAdmin)




from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import csv
from .models import Result, Result1


# Admin for Semester 1 (Result model)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        'roll_no', 'linear_algebra', 'oop_theory', 'oop_practical',
        'pakistan_studies', 'islamic_studies', 'digital_logic_theory',
        'digital_logic_practical', 'communication_skills'
    )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload-csv/', self.upload_csv, name="upload_csv"),
        ]
        return custom_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES.get("csv_file")
            if not csv_file.name.endswith('.csv'):
                self.message_user(request, "This is not a valid CSV file.", level='error')
                return HttpResponseRedirect(request.path)

            file_data = csv_file.read().decode("utf-8").splitlines()
            reader = csv.DictReader(file_data)
            for row in reader:
                Result.objects.update_or_create(
                    roll_no=row['roll_no'],
                    defaults={
                        'linear_algebra': row['linear_algebra'],
                        'oop_theory': row['oop_theory'],
                        'oop_practical': row['oop_practical'],
                        'pakistan_studies': row['pakistan_studies'],
                        'islamic_studies': row['islamic_studies'],
                        'digital_logic_theory': row['digital_logic_theory'],
                        'digital_logic_practical': row['digital_logic_practical'],
                        'communication_skills': row['communication_skills'],
                    }
                )
            self.message_user(request, "CSV file uploaded successfully.")
            return HttpResponseRedirect("../")

        return render(request, "admin/upload_csv.html", {'title': "Upload Semester 2 CSV"})


# Admin for Semester 2 (Result1 model)
class Result1Admin(admin.ModelAdmin):
    list_display = (
        'roll_no', 'applied_physics_theory', 'applied_physics_practical',
        'calculus_and_analytical_geometry', 'functional_english',
        'intro_to_info_and_comm_techns_theory', 'intro_to_info_and_comm_techns_practical',
        'programming_fundamentals_theory', 'programming_fundamentals_practical'
    )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload-csv/', self.upload_csv, name="upload_csv"),
        ]
        return custom_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES.get("csv_file")
            if not csv_file.name.endswith('.csv'):
                self.message_user(request, "This is not a valid CSV file.", level='error')
                return HttpResponseRedirect(request.path)

            file_data = csv_file.read().decode("utf-8").splitlines()
            reader = csv.DictReader(file_data)
            for row in reader:
                Result1.objects.update_or_create(
                    roll_no=row['roll_no'],
                    defaults={
                        'applied_physics_theory': row['applied_physics_theory'],
                        'applied_physics_practical': row['applied_physics_practical'],
                        'calculus_and_analytical_geometry': row['calculus_and_analytical_geometry'],
                        'functional_english': row['functional_english'],
                        'intro_to_info_and_comm_techns_theory': row['intro_to_info_and_comm_techns_theory'],
                        'intro_to_info_and_comm_techns_practical': row['intro_to_info_and_comm_techns_practical'],
                        'programming_fundamentals_theory': row['programming_fundamentals_theory'],
                        'programming_fundamentals_practical': row['programming_fundamentals_practical'],
                    }
                )
            self.message_user(request, "CSV file uploaded successfully.")
            return HttpResponseRedirect("../")

        return render(request, "admin/upload_csv.html", {'title': "Upload Semester 1 CSV"})


# Register both models in the Django admin interface
admin.site.register(Result, ResultAdmin)
admin.site.register(Result1, Result1Admin)
