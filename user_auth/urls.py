
from django.urls import path
from rest_framework.routers import DefaultRouter

# from user_auth.view.logout_view.LogoutView import LogoutView
from user_auth.view.login_registration.login import LoginView
from user_auth.view.login_registration.registration import RegisterView

from user_auth.views_sets.view_sets_user.user_views_set import *
from user_auth.views_sets.views_group.group import *
from user_auth.views_sets.views_student.student import *
from user_auth.views_sets.views_course.course_views import *
from user_auth.views_sets.views_lesson.lesson import *
from user_auth.views_sets.views_workers.stafff import *
from user_auth.views_sets.views_sets_pay.for_worker import *
from user_auth.views_sets.views_sets_pay.for_student import *
from user_auth.views_sets.views_workers.workers import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'group_homework', GroupHomeWorkViewsSet)
router.register(r'student_homework', StudentHomeworkViewSet)
router.register(r'lessons', LessonViewsSet)
router.register(r'study_days', StudyDayViewSet)
router.register(r'course_durations', CourseDurationViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'students', StudentViewSet)
router.register(r'parents', ParentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'mentors', MentorViewSet)
router.register(r'work_days', WorkDayViewSet)
router.register(r'position_levels', PositionLevelViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'worker_salary_payed', PayForWorkerViewSet)
router.register(r'worker_salary_waited_pay', WorkerSalaryWaitedPayViewSet)
router.register(r'staff', StaffViewsSet)
router.register(r'pay_for_student', PayStudentViewsSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('register/', RegisterView.as_view(), name='register'),
]


urlpatterns += router.urls
