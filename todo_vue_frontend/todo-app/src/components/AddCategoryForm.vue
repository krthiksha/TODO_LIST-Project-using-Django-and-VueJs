<template>
  <form>
          <div class="mb-3">
            <label for="category-name" class="form-label">Category Name
              <span style="color: red;">*</span>
            </label>
            <input type="text" class="form-control" v-model="newCategory.categoryName" placeholder="Category Name (required)" />
          </div>

          <div class="mb-3">
            <label for="category-description" class="form-label">Category Description</label>
            <textarea class="form-control" v-model="newCategory.categoryDescripition" placeholder="Category Description"></textarea>
          </div>
         
          <div class="d-flex justify-content-end mt-3">
            <button type="button" class="btn btn-secondary me-2" data-bs-dismiss="modal">Cancel</button>
            <button type="button " class="btn btn-primary" data-bs-dismiss="modal" @click="emitAddCategory">Save</button>
          </div>
          

        </form>
</template>

<script>
export default {
    data(){
        return {
            // store categories 
            newCategory: { categoryName: '', categoryDescripition: '' },
        }
    },
    methods: {
        emitAddCategory() {
        console.log("emitAddCategory method is triggered.  The New category :- ", this.newCategory)
        this.$emit('category-added', this.newCategory);   // send new task data to parent component
        // Optionally, clear the form or perform other UI updates
        this.newTask = { categoryName: '', categoryDescripition: '' };
        },
    },


}
</script>

<style>

</style>