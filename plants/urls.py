from django.urls import path
from . import views

app_name = 'plants'

urlpatterns = [
    path('places/create/', 
        views.PlaceCreateView.as_view(),
        name='create_place'),
    path('places/', 
        views.PlaceListView.as_view(), 
        name='list_place'),
    path('places/edit/<int:pk>', 
        views.PlaceUpdateView.as_view(),
        name='edit_place'),
    path('places/delete/<int:pk>',
        views.PlaceDeleteView.as_view(),
        name="delete_place"),
    path('majors/create/',
        views.MajorCreateView.as_view(),
        name='create_major'),
    path('majors/',
        views.Major.major_list,
        name='list_major'),
    path('majors/edit/<int:pk>',
        views.MajorUpdateView.as_view(),
        name='edit_major'),
    path('majors/delete/<int:pk>',
        views.MajorDeleteView.as_view(),
        name='delete_major'),
    path('employees/create/',
        views.EmployeeCreateView.as_view(),
        name='create_employee'),
    path('employees/',
        views.Employee.employee_list,
        name='list_employee'),
    path('employees/edit/<int:pk>',
        views.EmployeeUpdateView.as_view(),
        name='edit_employee'),
    path('employees/delete/<int:pk>',
        views.EmployeeDeleteView.as_view(),
        name='delete_employee'),
    path('criterias/create/',
        views.CriteriaCreateView.as_view(),
        name='create_criteria'),
    path('criterias/',
        views.Criteria.criteria_list,
        name='list_criteria'),
    path('criterias/edit/<int:pk>',
        views.CriteriaUpdateView.as_view(),
        name='edit_criteria'),
    path('criterias/delete/<int:pk>',
        views.CriteriaDeleteView.as_view(),
        name='delete_criteria'),
    path('evaluationtypes/create/', 
        views.EvaluationtypeCreateView.as_view(),
        name='create_evaluationtype'),
    path('evaluationtypes/', 
        views.EvaluationtypeListView.as_view(), 
        name='list_evaluationtype'),
    path('evaluationtypes/edit/<int:pk>', 
        views.EvaluationtypeUpdateView.as_view(),
        name='edit_evaluationtype'),
    path('evaluationtypes/delete/<int:pk>',
        views.EvaluationtypeDeleteView.as_view(),
        name="delete_evaluationtype"),
    path('places/<int:pk>/evaluationtypes', 
        views.Evaluation.place_detail_evaluationtype, 
        name='detail_place_evaluationtype'),
    path('places/<int:pk>/evaluationtypes/<int:evaluationtype_pk>/criterias', 
        views.Evaluation.place_detail_criteria, 
        name='detail_place_criteria'),
     path('places/<int:place_pk>/majors/<int:major_pk>/evaluationtypes/<int:evaluationtype_pk>', 
        views.Evaluation.place_detail_employee, 
        name='place_detail_employee'), 
    path('places/<int:place_pk>/evaluationtypes/<int:evaluationtype_pk>/majors/<int:major_pk>/be',
        views.Evaluation.basic_evaluation, 
        name='basic_evaluation'),
    path('places/<int:place_pk>/evaluationtypes/<int:evaluationtype_pk>/majors/<int:major_pk>/te', views.Evaluation.ticket_evaluation, name='ticket_evaluation'),
    path('places/<int:place_pk>/evaluationtypes/<int:evaluationtype_pk>/majors/<int:major_pk>/mme',
        views.Evaluation.medical_member_evaluation, 
        name='medical_member_evaluation'),
    path('places/<int:place_pk>/evaluationtypes/<int:evaluationtype_pk>/majors/<int:major_pk>/survey',
        views.Evaluation.survey_evaluation, 
        name='survey_evaluation'), 
    path('places/<int:place_pk>/evaluationtypes/<int:evaluationtype_pk>/majors/<int:major_pk>/survey/print',
        views.Evaluation.survey_evaluation_print, 
        name='survey_evaluation_print'), 
    path('reports/', views.EvaluationView.reports, name='get_report'),
    path('reports/results/', views.EvaluationView.evaluation_result, name='evaluation_result'),
    path('reports/basicevaluation/edit/<int:pk>',
        views.EvaluationView.basic_evaluation_edit,
        name='basic_evaluation_edit'),
    path('reports/memberevaluation/edit/<int:pk>',
        views.EvaluationView.member_evaluation_edit,
        name='member_evaluation_edit'),
    path('reports/ticketevaluation/edit/<int:pk>',
        views.EvaluationView.ticket_evaluation_edit,
        name='ticket_evaluation_edit'),
    path('reports/surveyevaluation/edit/<int:pk>',
        views.EvaluationView.survey_evaluation_edit,
        name='survey_evaluation_edit'),
    path('reports/basicevaluation/delete/<int:pk>',
        views.BasicEvaluationDeleteView.as_view(), 
        name="basic_evaluation_delete"),
    path('reports/memberevaluation/delete/<int:pk>',
        views.MemberEvaluationDeleteView.as_view(), 
        name="member_evaluation_delete"),
    path('reports/ticketevaluation/delete/<int:pk>',
        views.TicketEvaluationDeleteView.as_view(),
        name="ticket_evaluation_delete"),
    path('reports/delete', views.EvaluationView.delete_interval,
        name='delete_interval'),
    path('reports/ticketevaluation/delete/ticket/<int:ticket>',
        views.EvaluationView.delete_ticket,
        name='delete_ticket'),
    path('reports/surveyevaluation/delete/voter',
        views.EvaluationView.delete_survey,
        name='delete_survey'),
    path('reports/memberevaluation/delete/major/<int:major>',
        views.EvaluationView.delete_member_evaluation_major,
        name='member_evaluation_delete_major'),
    path('reports/basicevaluation/delete/major/<int:major>',
        views.EvaluationView.delete_basic_evaluation_major,
        name='basic_evaluation_delete_major'),
    path('get_majors', views.get_majors, name='get_majors'),
]
