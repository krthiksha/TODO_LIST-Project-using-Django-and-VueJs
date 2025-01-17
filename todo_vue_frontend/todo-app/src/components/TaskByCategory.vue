<template>
    <!-- card for category and task filtering   -->
    <div class="card">
            <div class="card-header m-2">
                <b>Filter Task By Category</b>
            </div>
            <!-- <br> -->
            <div class="d-flex justify-content-between align-items-center">
                    <div class="col-md-6">

                        <label for="categoryDropdown" class="form-label">Category</label>
                        <select id="categoryDropdown" class="form-select" v-model="filter.category" @change="fetchTasksOfCategory()">
                            <option value="" disabled>select a category</option>
                            <option v-for="category_item in taskCategories" :key="category_item.id" :value="category_item.id">
                                {{  category_item.categoryName }}   
                            </option>
                        </select>
                    </div>

                    <div class="col-md-6">
                        <label for="tasksDropdown" class="form-label">Tasks</label>
                        
                        <select id="tasksDropdown" class="form-select" v-model="filter.tasksOfCategory"  >
                            <option value="" disabled>select a task</option>
                            <option v-for="task in allTasks" :key="task.id" :value="task.id">
                                {{  task.name }}   
                            </option>
                        </select>
                    </div>
                    
            </div>
            <div class="card-body">
                <!-- <a href="#" class="btn btn-primary" @click="FetchSelectedTask">Fetch Task</a> -->
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#taskDetail" @click="FetchSelectedTask">
                Fetch Task
                </button>
            </div>

            <!-- Button trigger modal -->
            <!-- <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#taskDetail" @click="FetchSelectedTask">
            Launch demo modal
            </button> -->

            <!-- Modal -->
            <div class="modal fade" id="taskDetail" tabindex="-1" aria-labelledby="taskDetailLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="taskDetailLabel">Task Details</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div v-if="ShowEditForm" class="modal-body">
                    <EditForm  :currentTask="selectedTask" :taskCategories="taskCategories" @update-task="UpdateTask" />
                </div>
                <div v-else>
                    <div  class="modal-body">
                        <p>No more tasks to show</p>
                    </div>
                    <div  class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    </div>
                </div>
                </div>
            </div>
            </div>     
    </div>


</template>

<script>
import axios from 'axios';
import EditForm from './EditForm.vue';

import { useToastr } from '@/toastr';
// define toastr
const toastr = useToastr();

export default {
    components: { EditForm },
    props: {
              taskCategories: {
                type: Array,
                required: true
              },
                  
        },
    data() {
        return{
            // to store user data
            filter: {
                category:'',
                tasksOfCategory:'',
            },
            // to store all tasks of selected category from API 
            allTasks : [], 
            // to store details of particular task
            selectedTask : [],

            // modalToggle: '',
            ShowEditForm: false,
        }
    },

    methods: {
        // Call API for fetch task based on category selection 
        async fetchTasksOfCategory(){
            console.log("fetchTasksOfCategory Method is Triggered")
            const category_id = this.filter.category;  //when user selects category the id will be stored from value to filter.category 
            console.log("the category id : ",category_id)

            // in case of no id passed 
            if (!category_id){
                this.allTasks = [] //clear all tasks
                return;
            }

            // calling api to fetch tasks by category 
            await axios
            .get(`tasksByCategory/${category_id}/`)
            .then(response=>{
                console.log("the tasksbyCategory Response data: ",response.data)
                this.allTasks = response.data
            })
            .catch(error => {
                console.log("Error fetching tasks based on category: ",error);
            })
        },

        // Call API to get the details of selected Task
        async FetchSelectedTask() {
            console.log("FetchSelectedTask Method is Triggered")
            const selected_task_id = this.filter.tasksOfCategory

            if (!selected_task_id){
                // this.modalToggle=false
                console.log("Select the task !!")
                toastr.error("Please select the task and Try again!")
                return;
            } else {
                console.log("the selected Task ID : ", selected_task_id)
                await axios
                .get(`task-detail/${selected_task_id}/`)
                .then(response => {
                    this.selectedTask = response.data
                    console.log("Task Details: ",this.selectedTask)

                    // this.modalToggle="modal"
                    this.ShowEditForm=true

                    // toastr.success("Task Details Fetched Successfully!")

                })
                .catch(error => {
                    console.log("Error Fetching the details of selected task: ",error)
                })
            }
                
                
        },

        // updating the task by emiting it to the parent 
        UpdateTask (updatedData) {
            console.log("update task Method Triggered , emit the UpdateTask function to parent component!", updatedData)
            this.$emit('emit-update-task', updatedData)

        }

    }

}
</script>

<style>

</style>





