from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 

from .serializers import TaskSerializer, CategorySerializer
from .models import Task, Category

# Create your views here.

#api view decorator 
@api_view(['GET'])   #only allow the GET method here
def apiOverview(request):
    # URL patterns
    api_urls = {
        'List of tasks': '/task-list/',
        'Particular task' : '/task-detail/<str:pk>/',
        'Create' : '/task-create',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/', 
         
        'Task Category': 'task-category-list/',
        'Particular Task Category': 'category/search/<str:pk>/',
        'Task Category Create': 'category/add/',
        'Task Category Update':'category/update/<str:pk>/',
        'Task Category Delete':'category/delete/<str:pk>/',
        
        'Filter Task By Category':'tasksByCategory/<str:pk>/',
        
        'Count of the Status': 'statusCount/',
        
        
    }
    return Response(api_urls)
    # return Response("API BASE POINT", safe=False)  #safe --> ?


# GET :- all the tasks
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')  #orderby --> latest data will come 1st (LIFO)
    serializer = TaskSerializer(tasks, many=True)  ## True -> query for all items
    return Response(serializer.data, status=status.HTTP_200_OK)

# GET :- PARTICULAR task
@api_view(['GET'])
def taskDetail(request,pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"Error": "Task Not Found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TaskSerializer(task, many=False)  ## Fasle -> query for 1 item
    return Response(serializer.data, status=status.HTTP_200_OK)

# CREATE task
@api_view(['POST'])
def taskCreate(request):
    # if request.method == 'POST':
        # ----------using Plain Django Queries
        data = request.data 
        # validate data manually
        name = data.get('name')
        description = data.get('description')
        taskStatus = data.get('status') 
        priority = data.get('priority') 
        category_id = data.get('category')  # Expecting the category ID
        
        categoryInstance = None
        # Validate and retrieve the category instance
        if category_id:
            try:
                categoryInstance = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                return Response({"Error": "Category Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        if name: 
            # create task using ORM
            task = Task.objects.create(name=name, description=description, status=taskStatus, category=categoryInstance, priority=priority)
            # serialize task
            serializer = TaskSerializer(task, many=False) #query for 1 item
            # return the response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        # if validation fails --> return
        return Response({"Error":"Invalid Data. Ensure Both The name and description of the Task are mentioned"}, status=status.HTTP_400_BAD_REQUEST)


# UPDATE task
@api_view(['PATCH'])
def taskUpdate(request,pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"Error": "Task Not Found"}, status=status.HTTP_404_NOT_FOUND)
    
    # plain django queries -- extract data
    data = request.data 
    name = data.get('name')
    description = data.get('description')
    taskStatus = data.get('status')
    priority = data.get('priority') 
    category_id = data.get('category')
    
    
    # Validate and retrieve the category instance
    if category_id:
        try:
            categoryInstance = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({"Error": "Category Not Found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        categoryInstance = None
    # else:
    #         return Response({"Error": "Category ID is required"}, status=status.HTTP_400_BAD_REQUEST)
           
    
    # manually update task fields
    if name is not None:
        task.name = name
    if description is not None:
        task.description = description
    if taskStatus is not None:
        task.status = taskStatus
    if priority is not None:
        task.priority = priority
    if categoryInstance is not None:
        task.category = categoryInstance
    
    # update task
    task.save()
    # serialize task
    serializer = TaskSerializer(task, many=False) # query for 1 item 
    
    return Response(serializer.data, status=status.HTTP_200_OK)
        

# DELETE task
@api_view(['DELETE'])
def taskDelete(request,pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"Error": "Task Not Found"}, status=status.HTTP_404_NOT_FOUND)
    
    task.delete()
    return Response("Task Successfully Deleted", status=status.HTTP_204_NO_CONTENT)



# get all category
@api_view(['GET'])
def getCategory(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

# get 1 category 
@api_view(['GET'])
def searchCategory(request,pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist:
        return Response({"Error":"Category Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data,  status=status.HTTP_200_OK)

# category creation
@api_view(['POST'])
def createCategory(request):
    data = request.data 
    category_name = data.get('categoryName')
    if category_name:
        category = Category.objects.create(categoryName=category_name)
        serializer = CategorySerializer(category,many=False)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response({"Error":"Invalid Data. Ensure that Category Name is provided."}, status=status.HTTP_400_BAD_REQUEST)
    

# category updation
@api_view(['PATCH'])
def updateCategory(request,pk):
        try:
            category = Category.objects.get(id=pk)
        except Category.DoesNotExist:
            return Response({"Error":"Category Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        category_name = data.get('categoryName')
        if category_name:
            category.categoryName = category_name
            
        category.save()
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)   

# category deletion
@api_view(['DELETE'])
def deleteCategory(request,pk):
    try:
        category = Category.objects.get(id=pk)
        category.delete()
        return Response("Category Successfully Deleted", status=status.HTTP_204_NO_CONTENT)

    except Category.DoesNotExist:
        return Response({"Error":"Category Not Found"}, status=status.HTTP_404_NOT_FOUND)
    
    
# Get tasks by category
@api_view(['GET'])
def tasksByCategory(request,pk):
    try:
        try:
            category = Category.objects.get(id=pk)
        except Category.DoesNotExist:
            return Response({"Error":"Category Not Found"}, status=status.HTTP_404_NOT_FOUND)
    
    
        tasks = Task.objects.filter(category=category)
        print(tasks)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ValueError:
        return Response({"Error":"Please enter a valid id (ID should be in Number)"})
    
    
# count API to get the count of status
@api_view(['GET'])
def countOfStatus(request):
    # all tasks
    tasks = Task.objects.all()
    # count
    tasks_count = tasks.count()
    completed_tasks = tasks.filter(status="completed").count()
    pending_tasks = tasks.filter(status="pending").count()
    in_process_tasks = tasks.filter(status="in_process").count()
    
    response_data = {
        "No_of_Tasks": tasks_count,
        "No_of_completed_tasks": completed_tasks,
        "No_of_pending_tasks": pending_tasks,
        "No_of_in_process_tasks": in_process_tasks,
    }
    
    return JsonResponse(response_data, status=status.HTTP_200_OK)

