<!-- <template>
    <div ref="editModal" class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Edit Task</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="task-name" class="col-form-label">Task Name:</label>
                <input type="text" class="form-control" id="task-name" v-model="task.name">
              </div>
              <div class="mb-3">
                <label for="task-description" class="col-form-label">Description:</label>
                <textarea class="form-control" id="task-description" v-model="task.description"></textarea>
              </div>
              <div class="mb-3">
                <label for="task-status" class="col-form-label">Task Status:</label>
                <select id="inputState" class="form-select" v-model="task.status">
                  <option value="PENDING">PENDING</option>
                  <option value="COMPLETED">COMPLETED</option>
                </select>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            <button type="button" class="btn btn-primary" @click="updateTask">Update</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'EditModal',
    props: {
      task: {
        type: Object,
        required: true
      }
    },
    mounted() {
      // Initialize the Bootstrap modal
      this.modalInstance = new bootstrap.Modal(this.$refs.editModal);
    },
    methods: {
      // Emits the custom event 'update-task' with the current task data
      updateTask() {
        this.$emit('update-task', this.task);
        this.modalInstance.hide();  // Hide the modal after updating the task
      },
      showModal() {
        this.modalInstance.show();  // Show the modal programmatically
      }
    }
  };
  </script>
  
  <style></style>
   -->

<!--  NEW ONE UPDATED :01 .................. -->
   
<template>
    <div>
      <form v-if="currentTask">
        
        <div class="mb-3">
          <label for="task-name" class="col-form-label">Task Name:</label>
          <input type="text" class="form-control" id="task-name" v-model="currentTask.name">
        </div>

        <div class="mb-3">
            <label for="task-category" class="form-label">Task Category</label>
            <select class="form-select"  v-model="currentTask.category.id">
              <option value="" disabled>select a category</option>
              <option v-for="category_item in taskCategories" :key="category_item.id" :value="category_item.id">
                {{  category_item.categoryName }}   
              </option>
            </select>
          </div>

        <div class="mb-3">
          <label for="task-description" class="col-form-label">Description:</label>
          <textarea class="form-control" id="task-description" v-model="currentTask.description"></textarea>
        </div>
        
        <div class="mb-3">
            <label for="task-status" class="form-label">Priority Level</label>
            <select class="form-select" v-model="currentTask.priority">
              <option value="high">High</option>
              <option value="medium">Medium</option>
              <option value="low">Low</option>
            </select>

          </div>

        <div class="mb-3">
          <label for="task-status" class="col-form-label">Task Status:</label>
          <select id="inputState" class="form-select" v-model="currentTask.status">
            <option value="pending">Pending</option>
            <option value="in_process">In Process</option>
            <option value="completed">Completed</option>
          </select>
        </div>
        
        <!-- footer Buttons -->
        <!-- <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
              <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="emitUpdateTask()">Update</button>
        </div> -->
         <!-- Flexbox for footer -->
         <div class="d-flex justify-content-end mt-3">
            <button type="button" class="btn btn-secondary me-2" data-bs-dismiss="modal">Cancel</button>
            <button type="button" class="btn btn-primary" data-bs-dismiss="modal"  @click="emitUpdateTask()">Update</button>
          </div>
      </form>
    </div>
  </template>
  
<script>
  export default {
    name: 'EditForm',
    props: {
      currentTask: {
        type: Object,
        required: true
      },
      taskCategories: {
        type: Array,
        required: true
      }
    },
    methods: {
      // sending currentTask data to parent component
      emitUpdateTask(){
        console.log("emitUpdateTask method is triggered.  The task sent :- ", this.currentTask)
        this.$emit('update-task',this.currentTask)
      }
    }

  
  };
</script>

