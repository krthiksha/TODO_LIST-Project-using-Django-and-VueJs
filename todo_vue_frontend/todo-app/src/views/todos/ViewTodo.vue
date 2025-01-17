<template>
    <!-- loading spinner -->
    <div v-if="loading" class="d-flex justify-content-center align-items-center my-3">
        <div class="spinner-border text-primary me-2" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
        <div>
            <b>Loading...</b>
        </div>
    </div>

    

    <!-- todo app container -->
    <div class="container mt-4">
        <!-- todo heading: container which justify space b/w heading and button -->
        <div class="d-flex justify-content-between align-items-center mb-3" >
            <div class="d-flex align-items-center">
                <h2><i class="bi bi-card-checklist"></i> To-Do List</h2>
                
                <!-- BreadCrump -->
                <nav aria-label="breadcrumb" class="d-inline-block ms-4">
                    <ol class="breadcrumb bg-transparent m-0 p-0">
                        <li class="breadcrumb-item">
                            <router-link to="/dashboard">
                                <i class="fas fa-home me-1"></i>Home
                            </router-link>
                        </li>
                        <li class="breadcrumb-item active" aria-current="page">
                            <i class="bi bi-check2-circle"></i> To-Do List
                        </li>
                    </ol>
                </nav>
            </div>
            <!-- <button type="button" class="btn btn-primary">Add Task</button> -->
            <!-- ADD TASK Button  -->
            <button type="button" 
            class="btn btn-primary" 
            data-bs-toggle="modal" 
            data-bs-target="#TaskModal"
            @click="AddTask">
            Add Task
            </button>

        </div>


        <!-- filter task by category : child component -->
        <!-- :allTasks="tasks" -->
        <TaskByCategory :taskCategories="category" @emit-update-task="UpdateTask" />
        

        <!-- bootstrap table for to do tasks:  -->
        
        
        <!-- ag grid for to do tasks  -->
        <div class="ag-theme-quartz" style="height: 500px; width: 100%;">

            <!--style="width: 100%; height: 100%;"  -->
            <!-- style="width: 700px; height: 700px;" -->
            <ag-grid-vue
            :columnDefs="tasksColumnNames"
            :rowData="tasks"
            :defaultColDef="defaultColDef"
            :rowSelection="'multiple'"
            :pagination="true"
            :gridOptions="gridOptions"
            class="ag-theme-quartz"
            style=" height: 500px;"
            ></ag-grid-vue>
        </div>


        <!-- MODAL -->
        <div class="modal fade" id="TaskModal" tabindex="-1" aria-labelledby="TaskModalLabel" aria-hidden="true">
            <div class="modal-dialog ">
                <div class="modal-content">

                <!--  EDIT TASK  -->
                <div v-if="ShowEditForm">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="TaskModalLabel">Edit Task</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" @click="closeEditForm"></button>
                    </div>
                    <div class="modal-body">
                        <EditForm  :currentTask="selectedTask" :taskCategories="category" @update-task="UpdateTask" />
                    </div>
                </div>

                <!--  ADD TASK  -->
                <div v-if="ShowAddTaskForm">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="TaskModalLabel">Create New Task</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <AddTaskForm @task-added="CreateTask"  :taskCategories="category"/>
                    </div>
                </div>

                </div>
            </div>
        </div>



    </div>
</template>
  
<script>
// importing child components
import AddTaskForm from '@/components/AddTaskForm.vue';
import EditForm from '@/components/EditForm.vue';
import TaskByCategory from '@/components/TaskByCategory.vue';

import axios from 'axios';
import { error } from 'jquery';

import { useToastr } from '@/toastr';

// aggrid
import { AgGridVue } from 'ag-grid-vue3'; // Import AG Grid Vue component


// define toastr
const toastr = useToastr();

export default {
      name: "viewTodo",
      components: { EditForm , AddTaskForm , AgGridVue, TaskByCategory },
      data() {
        return{
            tasks: [],
            selectedTask: {
                category: ''
            },  // used to store current task
            ShowEditForm: false,
            ShowAddTaskForm: false,
            loading: false,
            category: [],

            // Ag-grid data's-------------------
            tasksColumnNames: [
                { headerName: "Task", field: "name" , checkboxSelection: true },
                { headerName: "Category", field: "category.categoryName" },
                { headerName: "Task Description", field: "description" },
                { headerName: "Priority Level", field: "priority" },

                // { headerName: "Deadline", field: "due_date",
                //   cellRenderer: (params) =>{
                //     console.log(params.value,"value data")
                //     // new -- create new instance of object , date() -- converts String into Date
                //     const dueDate = new Date(params.value);
                //     const today = new Date();
                //     today.setHours(0,0,0,0);
                //     //  
                //     if (dueDate < today )  {
                //         return `<span style="color:red">${params.value}</span>`
                //     } else {
                //         return params.value;
                //     }
                //   }
                // },
                
                { headerName: "Status", 
                  field: "status", 
                  cellClass: "text-left", // cellClass property to align text in grid 
                  cellRenderer: (params) => { 
                        let status = params.value; // The status value, e.g: 'C', 'P', 'I'
                        let displayText = '';
                        let style = '';

                        if (status === 'completed') {
                        displayText = 'Completed';
                        style = 'color: green; ';
                        } else if (status === 'pending') {
                        displayText = 'Pending';
                        style = 'color: crimson; ';
                        } else if (status === 'in_process') {
                        displayText = 'In Process';
                        style = 'color: darkorange; ';
                        }
                        return `<span style="${style}" ><i class="bi bi-circle-fill fs-14"></i></span> ${displayText}`;
                    }
                },
                {
                    headerName: "Edit Task",
                    sortable: false,
                    filter: false,
                    cellRenderer: (params) => {
                        const taskId = params.data.id;
                        //  document.querySelector('#TaskModal') --> Finds the modal element with the ID TaskModal.
                        // dispatchEvent--> Dispatches a custom event named openModal to the modal.
                        return `<button type="button" class="btn btn-outline-primary mr-3 btn-sm" 
                                    data-bs-toggle="modal" 
                                    data-bs-target="#TaskModal"
                                    onclick="document.querySelector('#TaskModal').dispatchEvent(new CustomEvent('openModal', { detail: ${taskId} }))">
                                    <i class="bi bi-pencil-fill"></i>
                                </button>`;
                    },
                },
                {
                    headerName: "Delete Task",
                    cellRenderer: (params) => {
                        const taskId = params.data.id;
                        return `<button type="button" 
                                class="btn btn-outline-danger btn-sm"
                                data-task-id="${taskId}"
                                ><i class="bi bi-trash3-fill"></i></button>`

                    },
                },
            ],
            defaultColDef: {
                filter: true,
                sortable: true,
                resizable: true,
            },
            gridOptions: {
                onCellClicked: this.onGridCellClicked,
            }

        }
      },

      //mounte the getTaskList() method before calling the API  ****
      mounted() {
        this.getTaskList();
        this.getTaskCategory();   //calls GET category API 

        // opens edit modal
        document.querySelector('#TaskModal').addEventListener('openModal', (event) => {
            const taskId = event.detail;
            const task = this.tasks.find(t => t.id === taskId);
            if (task) {
                this.selectedTask = task;
                this.ShowEditForm = true;
                this.ShowAddTaskForm = false;
            }
        });
        
        
      },
      methods: {
        // ----------------Ag-grid Methods ---------------
        onGridCellClicked(event){
            // calling delete method from delete button grid cell
            if(event.colDef.headerName === "Delete Task"){
                // const taskId = event.eTarget.
                const taskId = event.event.target.getAttribute('data-task-id');
                if (taskId) {
                    console.log("delete method from delete button grid cell was Triggered and the Task id :", taskId)
                    this.DeleteTask(Number(taskId)); // Ensure taskId is a number if necessary
                }
            }
        },
        // --------------------- GET all Tasks -------------------
        // Calling Get API
        async getTaskList(){
            this.loading = true  // spinner -- loading..page symbol
            console.log("getTaskList Method is Triggered")
            await axios
            .get('/task-list/')     // get HTTP request
            .then(response=>{
                console.log("Data from Response: ",response.data)
                this.tasks = response.data
                console.log("Tasks Array: ",this.tasks)
            })
            .catch(error => {
                console.log("Error Fetching Tasks: ", error)
            })
            .finally(() => {
                this.loading = false
            })
    
        },

        // ----------------------EDIT TASK -------------------
        EditTask(taskItem) {
            this.ShowAddTaskForm = false;
            this.ShowEditForm = true; 
            console.log("EditTask Method is Triggered");
            this.selectedTask = {...taskItem}; //spread or rest operator -- to get copy of original data
            console.log("Task : ",this.selectedTask)
            
        },
        // Calling Update API 
        async UpdateTask(updatedTask) {
            this.loading = true  // spinner -- loading..page symbol
            console.log("UpdateTask Method is Triggered",updatedTask);
            // Ensure updatedTask is not undefined and contains an id
            if (!updatedTask || !updatedTask.id) {
                console.error("Invalid task data received:", updatedTask);
                return;
            }

            await axios
            .patch(`task-update/${updatedTask.id}/`, {   //manually sending the data's
                category: updatedTask.category.id,
                description: updatedTask.description,
                due_date: null,
                id: updatedTask.id,
                name: updatedTask.name,
                priority: updatedTask.priority,
                status: updatedTask.status
            })
            .then(response => {
                console.log("User updated-task : ",response.data);
                const index = this.tasks.findIndex(task => task.id === updatedTask.id);
                if (index !== -1) {  //if task.index not exist -> return -1
                    this.tasks[index] = response.data; 
                }
                // set editModal back to false
                this.ShowEditForm = false;
                console.log("Updated Task Array: ",this.tasks);

                // vue toast notification
                toastr.success("Task Updated Successfully!");
            })
            .catch(error => {
                console.log("Error Updating Task: ",error);
                // vue toast notification
                toastr.error("Failed to Update Task");
            })
            .finally(() => {
                this.loading = false
                this.getTaskList(); 
            })

        },
        closeEditForm ()  {
            this.ShowEditForm = false;
        },

        // ----------------------ADD TASK -------------------
        AddTask() {
            console.log("AddTask Method is Triggered");
            this.ShowEditForm = false;
            this.ShowAddTaskForm = true;
        },
        // CreateTask(newTask) {
        //     console.log("CreateTask Method is Triggered", newTask);
        // },

        // Calling Add Task API 
        async CreateTask(newTask) {
            this.loading = true  // spinner -- loading..page symbol
            console.log("CreateTask Method is Triggered");
            await axios
            .post('task-create/', newTask)
            .then(response => {
              console.log("Task Added: ",response.data);
              // vue toast notification
              toastr.success("Task Created Successfully!");
 
            })
            .catch(error => {
              console.log("Error Adding the Task : ",error);
              // vue toast notification
              toastr.error("Please fill in all required fields before submitting the task.")
            })
            .finally(() => {
                this.loading = false
                this.getTaskList();  // calling get api -- to get all data with updated task
            })

        },

        // ----------------------DELETE TASK -------------------
        // Calling Delete API
        async DeleteTask(taskId){
            if (confirm('Are you sure you want to delete the Task?')) {
                this.loading = true  // spinner -- loading..page symbol
                console.log("DeleteTask Method is Triggered");
                await axios
                .delete(`task-delete/${taskId}/`)
                .then(response => {
                    // to Remove the task in frontend VueJs --> use filter option
                    this.tasks = this.tasks.filter(task => task.id !== taskId)

                    console.log("Task Deleted Successfully!!")
                    console.log("Tasks Array After Deletion: ",this.tasks)

                    // vue toast notification
                    toastr.success("Task Deleted Successfully!");
                    
                })
            
                .catch(error => {
                    console.log("Error Deleting the Task: ", error)
                    // vue toast notification
                    toastr.error("Oops! Something went wrong while deleting the task. Please try again later.");
                })
                .finally(() => {
                    this.loading = false
                })
            }
            else {
                console.log("Task Deletion Cancelled!");

                // vue toast notification
                toastr.info("Task deletion has been canceled. The task remains unchanged.");
            }

        },

        // -----------------GET task Categories ---------------------------
        async getTaskCategory(){
            this.loading = true
            console.log("getTaskCategory Method is Triggered")
            await axios
            .get('category/list/')     // get HTTP request
            .then(response=>{
                console.log("Data from Response: ",response.data)
                this.category = response.data
                console.log("category Array: ",this.category)
            })
            .catch(error => {
                console.log("Error Fetching category: ", error)
            })
            .finally(()=>{
                this.loading = false
            })
        },


        // ----------------------------------
        // calling the "emitUpdateTask" method from EditForm component
        // emitUpdateTask() {
        //     this.$refs.EditForm.emitUpdateTask();
        // },


        // UpdateTask(){
        // //   console.log("new: ",NewTask);
        //   const index = this.tasks.findIndex(task => task.id === this.selectedTask.id);
        //   if (index != -1) {  //if task.index not exist -> return -1
        //     this.tasks[index] = {...this.selectedTask}; 
        //     // alert("The Task Updated Successfully.");
        //   }
        //   // set editModal back to false
        //   this.ShowEditForm = false;
        // },

        


        // async getTasks() {
        //     console.log("getTasks method triggered");
        //     await axios
        //         .get('get-tasks/')
        //         .then(response => {
        //         console.log("Fetched Task:", response.data);
        //         this.tasks = response.data;  // Adjust based on your API response
        //         console.log("Tasks Array:", this.tasks);
        //         })
        //         .catch(error => {
        //         console.log("Error fetching tasks:", error);
        //         });
        // },
        
        
        //  advanced method for calling backend  API 
        // async getTasks() {
        //     try {
        //         const response = await axios .get('get-tasks/')
        //         this.tasks = response.data
        //     }
        //     catch (error) {
        //         console.log(error)
        //     }
        // }


      }
  }
  
  
</script>


  
<style>
  h2{
      text-align: left;
  }
  

  .edit-btn {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
    border-radius: 4px;
}

.edit-btn:hover {
    background-color: #0056b3;
}

</style>
  
  



    
    