<template>
    <div class="todo-container">
      <h2>To-Do List</h2>
      <ul>
        <li v-for="(task, index) in tasks" :key="index">
          <input type="checkbox" v-model="task.completed">
          <span :class="{ completed: task.completed }">{{ task.text }}</span>
        </li>
      </ul>
      <input v-model="newTask" @keyup.enter="addTask" placeholder="Add a new task" />
      <button @click="addTask">Add Task</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        tasks: [
          { text: "Learn Vue.js", completed: false },
          { text: "Build a to-do app", completed: false },
        ],
        newTask: "",
      };
    },
    methods: {
      addTask() {
        if (this.newTask.trim() !== "") {
          this.tasks.push({ text: this.newTask, completed: false });
          this.newTask = "";
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .todo-container {
    text-align: left;
    max-width: 600px;
    margin: auto;
  }
  
  .completed {
    text-decoration: line-through;
  }
  
  input[type="checkbox"] {
    margin-right: 10px;
  }
  </style>
  