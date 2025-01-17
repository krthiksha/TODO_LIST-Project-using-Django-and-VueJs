from django.urls import path
from . import views

urlpatterns = [
                    # OVERVIEW
                    path('', views.apiOverview, name="api-overview"),
                    
                    # TASKS
                    path('task-list/', views.taskList, name="task-list"),
                    path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
                    path('task-create/', views.taskCreate, name="task-create"),
                    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
                    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
                    
                    # TASK CATEGORIESZ
                    path('category/list/', views.getCategory, name="task-category-list"),
                    path('category/search/<str:pk>/', views.searchCategory, name="task-category-search"),
                    path('category/add/', views.createCategory, name="task-category-create"),
                    path('category/update/<str:pk>/', views.updateCategory, name="task-category-update"),
                    path('category/delete/<str:pk>/', views.deleteCategory, name="task-category-delete"),
                    
                    # task by category
                    path('tasksByCategory/<str:pk>/', views.tasksByCategory, name="task-by-category"),
                    
                    # get count of status 
                    path('statusCount/', views.countOfStatus, name="count-of-status"),
                    
                    # path('get-tasks/', views.get_tasks)

              ]


