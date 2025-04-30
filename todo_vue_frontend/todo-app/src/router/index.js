import { createRouter, createWebHistory } from 'vue-router';

import TodoList from "../views/TodoList.vue";
import DashBoard from "../views/DashBoard.vue";
// import TodoCrud from "../views/TodoCrud.vue";
import ViewTodo from "../views/todos/ViewTodo.vue";
import AddTaskForm from '@/components/AddTaskForm.vue';
import TaskByCategory from '@/components/TaskByCategory.vue';
import Category from "../views/todos/Category.vue";

// import EditModal from '@/components/EditForm.vue';

const routes = [
  {
    path: '/',
    redirect: '/dashboard'
  },
  {
    path: '/todo',
    name: 'todo',
    component: TodoList
  },
  {
    path : '/dashboard',
    name: 'DashBoard',
    component :  DashBoard,
  },

  {
    path:'/view-todo',
    name: 'view',
    component: ViewTodo
  },
  {
    path: '/add-task',
    name: 'addTask',
    component: AddTaskForm
  },
  {
    path: '/task-by-category',
    name: 'taskByCategory',
    component: TaskByCategory
  },
  {
    path: '/category',
    name: 'category',
    component: Category 
  },

  // {
  //   path: "/edit-modal",
  //   name: 'EditModal',
  //   component: EditModal,

  // }
  // Uncomment and modify this section if you have an 'About' view
  // {
  //   path: '/about',
  //   name: 'about',
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router;
