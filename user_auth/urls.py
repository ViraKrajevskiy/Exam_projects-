from user_auth.views_sets import *
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import  DefaultRouter




from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_auth.views_sets.view_sets_user.user_views_set import *
from user_auth.views_sets.views_workers.stafff import StaffViewsSet

router = DefaultRouter()
# router.register(r'users', )
# router.register(r'group_homework', GroupHomeworkViewSet)
# router.register(r'student_homework', StudentHomeworkViewSet)
# router.register(r'rooms', RoomViewSet)
# router.register(r'lessons', LessonViewSet)
# router.register(r'study_days', StudyDayViewSet)
# router.register(r'course_durations', CourseDurationViewSet)
# router.register(r'courses', CourseViewSet)
# router.register(r'groups', GroupViewSet)
# router.register(r'students', StudentViewSet)
# router.register(r'parents', ParentsViewSet)
# router.register(r'teachers', TeacherViewSet)
# router.register(r'mentors', MentorViewSet)
# router.register(r'work_days', WorkDayViewSet)
# router.register(r'position_levels', PositionLevelViewSet)
# router.register(r'departments', DepartmentViewSet)
# router.register(r'worker_salary_payed', WorkerSalaryPayedViewSet)
# router.register(r'worker_salary_waited_pay', WorkerSalaryWaitedPayViewSet)
router.register(r'staff', StaffViewsSet)


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('teacher_api/',TeacherViewSet.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]