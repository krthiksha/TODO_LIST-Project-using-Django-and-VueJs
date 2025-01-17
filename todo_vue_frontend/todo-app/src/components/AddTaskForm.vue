<template>

          <div v-if="isAddTaskRoute" class="d-flex justify-content-between align-items-center mb-3" >
            
            <div class="d-flex align-items-center">
                <h2>
                   <i class="bi bi-plus-circle"></i>  Create New Task</h2>
                
                <!-- BreadCrump -->
                <nav aria-label="breadcrumb" class="d-inline-block ms-4">
                    <ol class="breadcrumb bg-transparent m-0 p-0">
                        <li class="breadcrumb-item">
                            <router-link to="/dashboard">
                                <i class="fas fa-home me-1"></i>Home
                            </router-link>
                        </li>
                        <li class="breadcrumb-item active" aria-current="page">
                          <router-link to="/view-todo">
                            <i class="bi bi-check2-circle"></i> To-Do List
                            </router-link>
                        </li>
                        <li class="breadcrumb-item active" aria-current="page"> 
                            <i class="bi bi-file-earmark-plus"></i>  Add Task
                        </li>
                    </ol>
                </nav>
            </div>
  
          </div>


   <form>
          <div class="mb-3">
            <label for="task-name" class="form-label">Task Name
              <span style="color: red;">*</span>
            </label>
            <input type="text" class="form-control" v-model="newTask.name" placeholder="Task Name (required)" />
          </div>
          
          <div class="mb-3">
            <label for="task-category" class="form-label">Task Category</label>
            <select class="form-select"  v-model="newTask.category">
              <option value="" disabled>select a category</option>
              <option v-for="category_item in taskCategories" :key="category_item.id" :value="category_item.id">
                {{  category_item.categoryName }}   
              </option>
            </select>
          </div>

          <div class="mb-3">
            <label for="task-description" class="form-label">Description</label>
            <textarea class="form-control" v-model="newTask.description" placeholder="Task Description"></textarea>
          </div>


          <div class="mb-3">
            <label for="task-status" class="form-label">Priority Level</label>
            <select class="form-select" v-model="newTask.priority">
              <option value="high">High</option>
              <option value="medium">Medium</option>
              <option value="low">Low</option>
            </select>

          </div>

          <div class="mb-3">
            <label for="task-status" class="form-label">Task Status</label>
            <select class="form-select" v-model="newTask.status">
              <option value="pending">Pending</option>
              <option value="in_process">In Process</option>
              <option value="completed">Completed</option>
            </select>

          </div>

          <div v-if="isAddTaskRoute" class="d-flex justify-content-end mt-3">
            <!-- <button type="button" class="btn btn-secondary me-2">Cancel</button> -->
            <button type="submit " class="btn btn-primary" @click="AddTask">Save</button>
          </div>
          <div v-else class="d-flex justify-content-end mt-3">
            <button type="button" class="btn btn-secondary me-2" data-bs-dismiss="modal">Cancel</button>
            <button type="button " class="btn btn-primary" data-bs-dismiss="modal" @click="emitAddTask">Save</button>
          </div>
          

        </form>
</template>

<script>
import { error } from 'jquery';
import axios from 'axios';


import { useToastr } from '@/toastr';
// define toastr
const toastr = useToastr();

export default {
  props: {
              taskCategories: {
                type: Array,
                required: true
              }
              
        },
  data(){
        return {
            // taskCategories: [],  // array to store categories 
            newTask: { name: '', category: '', description: '',  priority: 'medium',status: 'pending' },
        }
  },
  computed: {
        isAddTaskRoute() {
          return this.$route.path === '/add-task'
        },
  },

  // mounted() {
  //   this.getTaskCategory();
  // },

  methods: {
    emitAddTask() {
      console.log("emitAddTask method is triggered.  The New task :- ", this.newTask)
      this.$emit('task-added', this.newTask);   // send new task data to parent component
      // Optionally, clear the form or perform other UI updates
      this.newTask = { name: '', description: '',  category: '', status: 'pending' };
    },

    // Calling Add Task API 
    async AddTask() {



        console.log("AddTask Method is Triggered");
        await axios
        .post('task-create/', this.newTask)
        .then(response => {
          console.log("Task Added: ",response.data);
          this.$emit('task-added',response.data);   // send new task data to parent component
          // vue toast notification
          toastr.success("Task Created Successfully!");
          console.log("Task emitted to parent component");

        })
        .catch(error => {
          console.log("Error Adding the Task : ",error);
          // vue toast notification
          toastr.error("Please fill in all required fields before submitting the task.")
        });

    },

    // GET CATEGORY 
    // async getTaskCategory(){
    //         console.log("getTaskCategory Method is Triggered")
    //         await axios
    //         .get('category/list/')     // get HTTP request
    //         .then(response=>{
    //             console.log("Data from Response: ",response.data)
    //             this.taskCategories = response.data
    //             console.log("category Array: ",this.taskCategories)
    //         })
    //         .catch(error => {
    //             console.log("Error Fetching category: ", error)
    //         })
    //     },


  },
}
</script>

<style>

</style>









