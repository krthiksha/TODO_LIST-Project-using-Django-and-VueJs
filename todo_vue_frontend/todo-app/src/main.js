
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';

import { createApp } from "vue";
import App from "./App.vue";
import "animate.css/animate.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";
import "bootstrap/dist/js/bootstrap.js";
import router from "./router";
// import store from "./store";
import axios from "axios";
// import Notifications from "@kyvg/vue3-notification";
import "@fortawesome/fontawesome-free/css/all.css";
 
import "bootstrap/dist/css/bootstrap.css";
import "admin-lte/dist/css/adminlte.min.css";
import "admin-lte/plugins/jquery/jquery.min.js";
import "admin-lte/dist/js/adminlte.min.js";


import 'ag-grid-community/styles/ag-grid.css';
import "ag-grid-community/styles/ag-theme-quartz.css";


 
// let websocketURL = "";
 
if (process.env.NODE_ENV === "development") {
  // Change to port 8000  -- local host
  axios.defaults.baseURL = "http://localhost:8000/api/v1/"; 
} else {
  // for production 
  axios.defaults.baseURL = "https://todo-app-djangobackend.onrender.com/api/v1/";
}


const app = createApp(App).use(router);  //.mount('#app');
 
// app.config.globalProperties.$websocketURL = websocketURL;
// app.use(store).use(router).use(Notifications);
 
app.mount("#app");






// import { createApp } from 'vue'
// import App from './App.vue'
// import router from './router'

// //bootstrap
// import 'bootstrap/dist/css/bootstrap.min.css';
// import "admin-lte/dist/css/adminlte.min.css";
// import "admin-lte/plugins/jquery/jquery.min.js";
// import "admin-lte/dist/js/adminlte.min.js";

// // admin-lte
// // import 'admin-lte/dist/css/adminlte.min.css';
// // import 'admin-lte/dist/js/adminlte.min.js';
// // import 'admin-lte/plugins/jquery/jquery.min.js';

// createApp(App).use(router).mount('#app')
