# # from django.shortcuts import render, redirect
# # from .models import Result
# # from .forms import RollNumberForm

# # # Grade to grade point mapping
# # GRADE_POINTS = {
# #     'A+': 4.0, 'A': 4.0, 'A-': 3.7,
# #     'B+': 3.3, 'B': 3.0, 'B-': 2.7,
# #     'C+': 2.3, 'C': 2.0, 'C-': 1.7,
# #     'D+': 1.3, 'D': 1.0, 'F': 0.0,'I':0.0,
# # }

# # # Subject credit hours
# # CREDIT_HOURS = {
# #     'linear_algebra': 3,
# #     'oop_theory': 3,
# #     'oop_practical': 1,
# #     'pakistan_studies': 2,
# #     'islamic_studies': 2,
# #     'digital_logic_theory': 2,
# #     'digital_logic_practical': 1,
# #     'communication_skills': 2,
# # }

# # def calculate_gpa(result):
# #     total_points = 0
# #     total_credits = 0

# #     # Iterate through each subject, get grade points and calculate GPA
# #     for subject, credit in CREDIT_HOURS.items():
# #         grade = getattr(result, subject, None)  # Get the grade for the subject
# #         if grade and grade in GRADE_POINTS:     # Check if the grade is valid
# #             total_points += GRADE_POINTS[grade] * credit
# #             total_credits += credit

# #     # Avoid division by zero
# #     if total_credits == 0:
# #         return 0.0

# #     # Calculate GPA
# #     gpa = total_points / total_credits
# #     return round(gpa, 2)  # Round GPA to 2 decimal places


# # def roll_number_input(request):
# #     error_message = None

# #     if request.method == "POST":
# #         form = RollNumberForm(request.POST)
# #         if form.is_valid():
# #             roll_no = form.cleaned_data['roll_no']
# #             if Result.objects.filter(roll_no=roll_no).exists():
# #                 return redirect('result_page', roll_no=roll_no)
# #             else:
# #                 error_message = "No results found for this Roll Number."
# #     else:
# #         form = RollNumberForm()

# #     return render(request, 'input_roll_no.html', {'form': form, 'error_message': error_message})


# # def result_page(request, roll_no):
# #     try:
# #         result = Result.objects.get(roll_no=roll_no)
# #         gpa = calculate_gpa(result)  # Calculate GPA
# #     except Result.DoesNotExist:
# #         result = None
# #         gpa = None

# #     return render(request, 'result_page.html', {'result': result, 'roll_no': roll_no, 'gpa': gpa})



# from django.shortcuts import render, redirect
# from .models import Result, Result1
# from .forms import RollNumberForm

# # Grade to grade point mapping (same for both semesters)
# GRADE_POINTS = {
#     'A+': 4.0, 'A': 4.0, 'A-': 3.7,
#     'B+': 3.3, 'B': 3.0, 'B-': 2.7,
#     'C+': 2.3, 'C': 2.0, 'C-': 1.7,
#     'D+': 1.3, 'D': 1.0, 'F': 0.0, 'I': 0.0,
# }

# # Credit hours for Semester 1
# CREDIT_HOURS_SEMESTER_1 = {
#     'linear_algebra': 3,
#     'oop_theory': 3,
#     'oop_practical': 1,
#     'pakistan_studies': 2,
#     'islamic_studies': 2,
#     'digital_logic_theory': 2,
#     'digital_logic_practical': 1,
#     'communication_skills': 2,
# }

# CREDIT_HOURS_1 = {
#     'applied_physics_theory': 3,
#     'applied_physics_practical': 1,
#     'calculus_and_analytical_geometry': 3,
#     'functional_english': 2,
#     'intro_to_info_and_comm_techns_theory': 2,
#     'intro_to_info_and_comm_techns_practical': 1,
#     'programming_fundamentals_theory': 3,
#     'programming_fundamentals_practical': 1,
# }

# CREDIT_HOURS_2 = {
#     'linear_algebra': 3,
#     'oop_theory': 3,
#     'oop_practical': 1,
#     'pakistan_studies': 2,
#     'islamic_studies': 2,
#     'digital_logic_theory': 2,
#     'digital_logic_practical': 1,
#     'communication_skills': 2,
# }

# def roll_number_input(request):
#     error_message = None

#     if request.method == "POST":
#         form = RollNumberForm(request.POST)
#         if form.is_valid():
#             roll_no = form.cleaned_data['roll_no']
#             if Result.objects.filter(roll_no=roll_no).exists():
#                 return redirect('result_page', roll_no=roll_no)
#             else:
#                 error_message = "No results found for this Roll Number."
#     else:
#         form = RollNumberForm()

#     return render(request, 'input_roll_no.html', {'form': form, 'error_message': error_message})


# def calculate_gpa1(result):
#     total_points = 0
#     total_credits = 0

#     # Iterate through each subject, get grade points and calculate GPA
#     for subject, credit in CREDIT_HOURS_1.items():
#         grade = getattr(result, subject, None)  # Get the grade for the subject
#         if grade and grade in GRADE_POINTS:     # Check if the grade is valid
#             total_points += GRADE_POINTS[grade] * credit
#             total_credits += credit

#     # Avoid division by zero
#     if total_credits == 0:
#         return 0.0

#     # Calculate GPA
#     gpa = total_points / total_credits
#     return round(gpa, 2)  # Round GPA to 2 decimal places

# def calculate_gpa2(result):
#     total_points = 0
#     total_credits = 0

#     # Iterate through each subject, get grade points and calculate GPA
#     for subject, credit in CREDIT_HOURS_2.items():
#         grade = getattr(result, subject, None)  # Get the grade for the subject
#         if grade and grade in GRADE_POINTS:     # Check if the grade is valid
#             total_points += GRADE_POINTS[grade] * credit
#             total_credits += credit

#     # Avoid division by zero
#     if total_credits == 0:
#         return 0.0

#     # Calculate GPA
#     gpa = total_points / total_credits
#     return round(gpa, 2)  # Round GPA to 2 decimal places



# # # Result Page for both Semesters
# # def result_page(request, roll_no):
# #     try:
# #         result_1 = Result1.objects.get(roll_no=roll_no)  # For Semester 1
# #         gpa_1 = calculate_gpa1(result_1)
# #         # gpa_1 = calculate_gpa_semester_1(result_1)
# #     except Result1.DoesNotExist:
# #         result_1 = None
# #         gpa_1 = None

# #     try:
# #         result_2 = Result.objects.get(roll_no=roll_no)  # For Semester 2
# #         gpa_2 = calculate_gpa2(result_2)
# #         # gpa_2 = calculate_gpa_semester_2(result_2)
# #     except Result.DoesNotExist:
# #         result_2 = None
# #         gpa_2 = None

# #     return render(request, 'result_page.html', {
# #         'result_1': result_1, 'gpa_1': gpa_1, 
# #         'result_2': result_2, 'gpa_2': gpa_2,
# #         'roll_no': roll_no
# #     })

# def result_page(request, roll_no):
#     try:
#         result_1 = Result1.objects.get(roll_no=roll_no)  # For Semester 1
#         gpa_1 = calculate_gpa1(result_1)
#     except Result1.DoesNotExist:
#         result_1 = None
#         gpa_1 = None

#     try:
#         result_2 = Result.objects.get(roll_no=roll_no)  # For Semester 2
#         gpa_2 = calculate_gpa2(result_2)
#     except Result.DoesNotExist:
#         result_2 = None
#         gpa_2 = None

#     # Calculate CGPA: weighted average of GPA for both semesters
#     cgpa = None
#     if gpa_1 is not None and gpa_2 is not None:
#         cgpa = round((gpa_1 + gpa_2) / 2, 2)  # Simple average of both GPAs
#     elif gpa_1 is not None:
#         cgpa = gpa_1
#     elif gpa_2 is not None:
#         cgpa = gpa_2

#     return render(request, 'result_page.html', {
#         'result_1': result_1, 'gpa_1': gpa_1,
#         'result_2': result_2, 'gpa_2': gpa_2,
#         'cgpa': cgpa,  # Passing CGPA to the template
#         'roll_no': roll_no
#     })



from django.shortcuts import render, redirect
from django.db.models import F
from .models import Result, Result1
from .forms import RollNumberForm

# Grade to grade point mapping
GRADE_POINTS = {
    'A+': 4.0, 'A': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D': 1.0, 'F': 0.0, 'I': 0.0,
}

# Credit hours for subjects
CREDIT_HOURS = {
    'semester_1': {
        'applied_physics_theory': 3, 'applied_physics_practical': 1,
        'calculus_and_analytical_geometry': 3, 'functional_english': 2,
        'intro_to_info_and_comm_techns_theory': 2, 'intro_to_info_and_comm_techns_practical': 1,
        'programming_fundamentals_theory': 3, 'programming_fundamentals_practical': 1,
    },
    'semester_2': {
        'linear_algebra': 3, 'oop_theory': 3, 'oop_practical': 1,
        'pakistan_studies': 2, 'islamic_studies': 2, 'digital_logic_theory': 2,
        'digital_logic_practical': 1, 'communication_skills': 2,
    },
}

def roll_number_input(request):
    error_message = None
    form = RollNumberForm(request.POST or None)

    if form.is_valid():
        roll_no = form.cleaned_data['roll_no']
        if Result.objects.filter(roll_no=roll_no).exists():
            return redirect('result_page', roll_no=roll_no)
        error_message = "No results found for this Roll Number."

    return render(request, 'input_roll_no.html', {'form': form, 'error_message': error_message})

def calculate_gpa(result, semester):
    """Calculate GPA for a given semester."""
    total_points = sum(GRADE_POINTS.get(getattr(result, subject, ''), 0) * credit
                       for subject, credit in CREDIT_HOURS[semester].items())
    total_credits = sum(CREDIT_HOURS[semester].values())

    return round(total_points / total_credits, 2) if total_credits else 0.0

def result_page(request, roll_no):
    """Fetch results efficiently & compute GPA/CGPA."""
    result_1 = Result1.objects.filter(roll_no=roll_no).only(*CREDIT_HOURS['semester_1'].keys()).first()
    result_2 = Result.objects.filter(roll_no=roll_no).only(*CREDIT_HOURS['semester_2'].keys()).first()

    gpa_1 = calculate_gpa(result_1, 'semester_1') if result_1 else None
    gpa_2 = calculate_gpa(result_2, 'semester_2') if result_2 else None

    # Compute CGPA
    cgpa = round((gpa_1 + gpa_2) / 2, 2) if gpa_1 and gpa_2 else gpa_1 or gpa_2

    return render(request, 'result_page.html', {
        'result_1': result_1, 'gpa_1': gpa_1,
        'result_2': result_2, 'gpa_2': gpa_2,
        'cgpa': cgpa, 'roll_no': roll_no
    })
