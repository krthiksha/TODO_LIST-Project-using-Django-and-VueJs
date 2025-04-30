<template>
  <div id="app">
    <div class="wrapper">
      <!-- Main Header -->
      <nav class="main-header navbar navbar-expand navbar-white navbar-light">
    <!-- Left navbar links -->
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" data-widget="pushmenu" href="#" role="button"><i class="fas fa-bars"></i></a>
      </li>
      <li class="nav-item d-none d-sm-inline-block">
        <router-link to="/dashboard" class="nav-link">
                    <i class="fas fa-home me-1"></i>
                    <!-- <p>Home</p> -->
                  </router-link>
        <!-- <a href="index3.html" class="nav-link">Home</a> -->
      </li>
      <!-- <li class="nav-item d-none d-sm-inline-block">
        <a href="#" class="nav-link">Contact</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Help
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#">FAQ</a>
          <a class="dropdown-item" href="#">Support</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Contact</a>
        </div>
      </li> -->
    </ul>

    <!-- SEARCH FORM -->
    <!-- <form class="form-inline ml-3">
      <div class="input-group input-group-sm">
        <input class="form-control form-control-navbar" type="search" placeholder="Search" aria-label="Search">
        <div class="input-group-append">
          <button class="btn btn-navbar" type="submit">
            <i class="fas fa-search"></i>
          </button>
        </div>
      </div>
    </form> -->

    <!-- Right navbar links -->
    <ul class="navbar-nav ml-auto">
      <!-- Messages Dropdown Menu -->
      <!-- <li class="nav-item">
        <a href="#" class="nav-link"><b>Welcome !</b></a>
      </li> -->
      <li class="nav-item ">
        <router-link to="#" class="nav-link">
          <i class="fa-solid fa-right-to-bracket"></i>
        </router-link>
       
      </li>
      <!-- <li class="nav-item dropdown">
        <a class="nav-link" data-toggle="dropdown" href="#">
          <i class="far fa-comments"></i>
          <span class="badge badge-danger navbar-badge">3</span>
        </a>
        <div class="dropdown-menu dropdown-menu-lg dropdown-menu-right">
          <a href="#" class="dropdown-item" data-widget="pushmenu">
            
            <div class="media">
              <img
          src="https://content.jdmagicbox.com/comp/bangalore/73/080ppe03673/catalogue/velankani-software-pvt-ltd-electronic-city-bangalore-computer-software-developers-2rgz2h5-250.jpg"
          alt="AdminLTE Logo"
          class="brand-image img-circle elevation-3"
          style="opacity: 0.8"
        />
              <div class="media-body">
                <h3 class="dropdown-item-title">
                  Brad Diesel
                  <span class="float-right text-sm text-danger"><i class="fas fa-star"></i></span>
                </h3>
                <p class="text-sm">Call me whenever you can...</p>
                <p class="text-sm text-muted"><i class="far fa-clock mr-1"></i> 4 Hours Ago</p>
              </div>
            </div>
            
          </a>
          <div class="dropdown-divider"></div>
          
          <div class="dropdown-divider"></div>
          <a href="#" class="dropdown-item">
            
            <div class="media">
              <img src="dist/img/user3-128x128.jpg" alt="User Avatar" class="img-size-50 img-circle mr-3">
              <div class="media-body">
                <h3 class="dropdown-item-title">
                  Nora Silvester
                  <span class="float-right text-sm text-warning"><i class="fas fa-star"></i></span>
                </h3>
                <p class="text-sm">The subject goes here</p>
                <p class="text-sm text-muted"><i class="far fa-clock mr-1"></i> 4 Hours Ago</p>
              </div>
            </div>
           
          </a>
          <div class="dropdown-divider"></div>
          <a href="#" class="dropdown-item dropdown-footer">See All Messages</a>
        </div>
      </li>
      
      <li class="nav-item dropdown">
        <a class="nav-link" data-toggle="dropdown" href="#">
          <i class="far fa-bell"></i>
          <span class="badge badge-warning navbar-badge">15</span>
        </a>
        <div class="dropdown-menu dropdown-menu-lg dropdown-menu-right">
          <span class="dropdown-header">15 Notifications</span>
          <div class="dropdown-divider"></div>
          <a href="#" class="dropdown-item">
            <i class="fas fa-envelope mr-2"></i> 4 new messages
            <span class="float-right text-muted text-sm">3 mins</span>
          </a>
          <div class="dropdown-divider"></div>
          <a href="#" class="dropdown-item">
            <i class="fas fa-users mr-2"></i> 8 friend requests
            <span class="float-right text-muted text-sm">12 hours</span>
          </a>
          <div class="dropdown-divider"></div>
          <a href="#" class="dropdown-item">
            <i class="fas fa-file mr-2"></i> 3 new reports
            <span class="float-right text-muted text-sm">2 days</span>
          </a>
          <div class="dropdown-divider"></div>
          <a href="#" class="dropdown-item dropdown-footer">See All Notifications</a>
        </div>
      </li>
      <li class="nav-item">
        <a class="nav-link" data-widget="control-sidebar" data-slide="true" href="#" role="button"><i
            class="fas fa-th-large"></i></a>
      </li> -->
    </ul>
  </nav>

      <!-- Main Sidebar -->
      <aside class="main-sidebar sidebar-dark-primary elevation-4">
        <a href="/" class="brand-link">
          <img
            src="https://content.jdmagicbox.com/comp/bangalore/73/080ppe03673/catalogue/velankani-software-pvt-ltd-electronic-city-bangalore-computer-software-developers-2rgz2h5-250.jpg"
            alt="AdminLTE Logo"
            class="brand-image img-circle elevation-3"
            style="opacity: 0.8"
          />
          <span class="brand-text font-weight-light">TO-DO APP</span>
        </a>
        <!-- Sidebar content here -->
        <div class="sidebar">
          <!-- Sidebar Menu -->
          <nav class="mt-2">
            <ul
              class="nav nav-pills nav-sidebar flex-column"
              data-widget="treeview"
              role="menu"
              data-accordion="false"
              >
              <!-- Accounts -->
              <li class="nav-item text-left">
                <!-- <a href="#" class="nav-link"> -->
                  <router-link to="/dashboard" class="nav-link">
                    <i class="nav-icon fas fa-users me-2"></i>
                    <p>Dashboard</p>
                    
                    <!-- <i class="right fas fa-angle-left"></i> -->
                  </router-link>
                <!-- </a> -->
              </li>

              
              <!-- drop down  -->
              <!-- <li class="nav-item text-left">
                <a href="#" class="nav-link">
                  <i class="nav-icon fas fa-check"></i>
                  <p>
                    Old Todo
                    <i class="right fas fa-angle-left"></i>
                  </p>
                </a>
                <ul class="nav nav-treeview">
                  <li class="nav-item">
                    <router-link to="/todo" class="nav-link">
                      <i class="fas fa-list nav-icon"></i>
                      <p>View Todo</p>
                    </router-link>
                  </li>
                  <li class="nav-item">
                    <router-link to="/todo/add" class="nav-link">
                      <i class="fas fa-plus nav-icon"></i>
                      <p>Add New Task</p>
                    </router-link>
                  </li>
                </ul>
              </li> -->


              <!-- new drop down  -->
              <!-- drop down  -->
              <li class="nav-item text-left">
                <a href="#" class="nav-link">
                  <i class="nav-icon fas fa-check"></i>
                  <!-- <i class="fa-regular fa-clipboard-list-check"></i> -->
                  <p>
                     Tasks
                    <i class="right fas fa-angle-left"></i>
                  </p>
                </a>
                <ul class="nav nav-treeview">
                  <li class="nav-item">
                    <router-link to="/view-todo" class="nav-link">
                      <i class="fas fa-list nav-icon"></i>
                      <p>All Tasks </p>
                    </router-link>
                  </li>

                  <!-- <li class="nav-item">
                    <router-link to="/add-task" class="nav-link">
                      <i class="fas fa-plus nav-icon"></i>
                      <p>New Task</p>
                    </router-link>
                  </li> -->

                  <li class="nav-item">
                    <router-link to="/category" class="nav-link">
                      <i class="fa-sharp fa-solid fa-layer-group nav-icon"></i>
                      <p>Categories</p>
                    </router-link>
                  </li>

                </ul>
              </li>
              
            </ul>
          </nav>
          <!-- /.sidebar-menu -->
        </div>
      </aside>


      <!-- Content Wrapper -->
      <div class="content-wrapper">
        <!-- Your page content here -->
        <router-view/>
        
      </div>

      <!-- Main Footer -->
      <footer class="main-footer">
        <!-- Footer content here -->
      </footer>
    </div>
    <notifications position="bottom right" classes="alert" />
  </div>
</template>

<script>


// import LoginForm from "./views/LoginForm.vue";

export default {
  name: "App",
  components: {
 
  },
  computed: {
    activeRoute() {
      return this.$route.path;
    },
  },
};
</script>

<style>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');
@import url('https://cdn.jsdelivr.net/npm/admin-lte@3.1.0/dist/css/adminlte.min.css');

html, body {
  height: 100%;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
}

.wrapper {
  min-height: 100%;
  display: flex;
  flex-direction: column;
}

.content-wrapper {
  flex: 1;
  padding: 20px;
}

.main-header, .main-sidebar, .main-footer {
  flex-shrink: 0;
}
</style>
