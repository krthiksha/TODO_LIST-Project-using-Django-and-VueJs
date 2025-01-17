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
                <h2>
                    <!-- <i class="bi bi-card-checklist"></i> -->
                    Category</h2>
                
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
                            <!-- <i class="bi bi-check2-circle"></i>  -->
                            <i class="bi bi-tags"></i>
                            Category
                        </li>
                    </ol>
                </nav>
            </div>
            <!-- <button type="button" class="btn btn-primary">Add Task</button> -->
            <!-- ADD TASK Button  -->
            <button type="button" 
            class="btn btn-primary" 
            data-bs-toggle="modal" 
            data-bs-target="#CategoryModal"
            @click="AddCategory">
            Add Category
            </button>

        </div>

        <!-- ag grid for to do tasks  -->
        <div class="ag-theme-quartz" style="height: 500px; width: 100%;">

        <!-- :gridOptions="gridOptions" -->
            <ag-grid-vue
            :columnDefs="categoryColumnNames"
            :rowData="category"
            :defaultColDef="defaultColDef"
            :rowSelection="'multiple'"
            :pagination="true"
            :gridOptions="gridOptions"
            class="ag-theme-quartz"
            style=" height: 500px;"
            ></ag-grid-vue>
        </div>

        <!-- MODAL -->
        <div class="modal fade" id="CategoryModal" tabindex="-1" aria-labelledby="CategoryModalLabel" aria-hidden="true">
            <div class="modal-dialog ">
                <div class="modal-content">

                <!--  ADD TASK  -->
                <div>
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="CategoryModalLabel">Create Category</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <AddCategoryForm @category-added="CreateCategory"  />
                    </div>
                </div>

                </div>
            </div>
        </div>




    </div>
  
</template>

<script>
import axios from 'axios';
import { error } from 'jquery';

import { useToastr } from '@/toastr';
// define toastr
const toastr = useToastr();

// aggrid
import { AgGridVue } from 'ag-grid-vue3'; 
import AddCategoryForm from '@/components/AddCategoryForm.vue';

export default {
    name: "category",
    components: { AgGridVue, AddCategoryForm },
    data(){
        return {
            category: [],
            loading: false,

            categoryColumnNames: [
                { headerName: "Category Name", field: "categoryName" , checkboxSelection: true , flex:1},
                { headerName: "Category Description", field: "categoryDescripition", flex:2 },

                {
                    headerName: "Delete Task",
                    cellRenderer: (params) => {
                        const categoryId = params.data.id;
                        return `<button type="button" 
                                class="btn btn-outline-danger btn-sm"
                                data-category-id="${categoryId}"
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
    mounted() {
        this.getCategory();
    },
    methods: {
        // ----------------Ag-grid Methods ---------------
        onGridCellClicked(event){
            // calling delete method from delete button grid cell
            if(event.colDef.headerName === "Delete Task"){
                // const taskId = event.eTarget.
                const categoryID = event.event.target.getAttribute('data-category-id');
                if (categoryID) {
                    console.log("delete method from delete button grid cell was Triggered and the category id :", categoryID)
                    this.DeleteCategory(Number(categoryID)); // Ensure taskId is a number if necessary
                }
            }
        },
        // get all category 
        async getCategory(){
            this.loading = true,
            console.log("getCategory Method Triggered")
            await axios
            .get('category/list/')
            .then(response => {
                console.log("the response data: ", response.data)
                this.category = response.data
            })
            .catch(error => {
                console.log("Error fetching the category: ",error)
            })
            .finally(()=>{
                this.loading = false
            })
        },

        // create new category 
        async CreateCategory(data){
            this.loading = true
            console.log("CreateCategory method triggered and the data : ", data)
            await axios
            .post('category/add/',data)
            .then(response => {
                console.log("The response data is : ",response.data)
            })
            .catch(error => {
                console.log("Error creating category:", error)
            })
            .finally(()=>{
                this.loading = false,
                this.getCategory();
            })
        },

        // delete a category 
        async DeleteCategory(categoryID){
            if (confirm("Are you sure you want to delete the category?")) {
                console.log("DeleteCategory Method is Triggered")
                await axios
                .delete(`category/delete/${categoryID}/`)
                .then(response => {
                    this.category = this.category.filter(category => category.id !== categoryID)
                    console.log("category Deleted Successfully!!")
                    console.log("category Array After Deletion: ",this.category)

                        // vue toast notification
                    toastr.success("Category Deleted Successfully!");

                })
                .catch(error => {
                    console.log("Error deleting category: ",error)
                    toastr.error("Oops! Something went wrong while deleting the category. Please try again later.");
    
                })
            } else {
                console.log("Category Deletion Cancelled!");
                toastr.info("Category deletion has been canceled. The Category remains unchanged.");
            
            }
        }
    }

}
</script>

<style>

</style>