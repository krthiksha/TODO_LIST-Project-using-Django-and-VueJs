<template>

  <div class="container mt-4">
        <!-- todo heading: container which justify space b/w heading and button -->
        <div class="d-flex justify-content-between align-items-center mb-3" >
            <div class="d-flex align-items-center">
                <h2>Dashboard</h2>
                <!-- BreadCrump -->
                <nav aria-label="breadcrumb" class="d-inline-block ms-4">
                    <ol class="breadcrumb bg-transparent m-0 p-0">
                        <li class="breadcrumb-item">
                            <router-link to="/dashboard">
                                <i class="fas fa-home me-1"></i>Home
                            </router-link>
                        </li>
                    </ol>
                </nav>
            </div>
        </div>

        <!-- Count of Status -->
        <div class="d-flex justify-content-between align-items-center mb-3"  style="display: flex; gap: 30px; justify-content: space-between;">
            <!-- <div class="info-box">
            <span class="info-box-icon bg-info"><i class="far fa-bookmark"></i></span>
            <div class="info-box-content">
                <span class="info-box-text">Bookmarks</span>
                <span class="info-box-number">41,410</span>
                <div class="progress">
                <div class="progress-bar bg-info" style="width: 70%"></div>
                </div>
                <span class="progress-description">
                70% Increase in 30 Days
                </span>
            </div>
            </div> -->

            <div class="info-box bg-success">
            <span class="info-box-icon">
                <!-- <i class="far fa-thumbs-up"></i> -->
                <i class="fa-regular fa-circle-check"></i>
            </span>
            <div class="info-box-content">
                <span class="info-box-text">Completed</span>
                <span class="info-box-number">{{ this.count.No_of_completed_tasks }}</span>
                <div class="progress">
                <div class="progress-bar" :style="{width: completedPercent + '%'}"></div>
                </div>
                <span class="progress-description">
                    {{ completedPercent }}% Tasks are Completed
                </span>
            </div>
            </div>

            <div class="info-box bg-gradient-info">
            <span class="info-box-icon">
                <!-- <i class="far fa-calendar-alt"></i> -->
                <i class="fa-solid fa-spinner"></i>
            </span>
            <div class="info-box-content">
                <span class="info-box-text">In-Process</span>
                <span class="info-box-number">{{ this.count.No_of_in_process_tasks }}</span>
                <div class="progress">
                <div class="progress-bar" :style="{width: inProcessPercent +'%'}"></div>
                </div>
                <span class="progress-description">
                {{ inProcessPercent }}% Tasks are in-process
                </span>
            </div>
            </div>

            <div class="info-box bg-gradient-danger">
            <span class="info-box-icon">
                <!-- <i class="far fa-calendar-alt"></i> -->
                <i class="fa-solid fa-circle-exclamation"></i>
            </span>
            <div class="info-box-content">
                <span class="info-box-text">Pending</span>
                <span class="info-box-number">{{ this.count.No_of_pending_tasks }}</span>
                <div class="progress">
                <div class="progress-bar" :style="{width: pendingPercent + '%'}"></div>
                </div>
                <span class="progress-description">
                {{ pendingPercent }}% Tasks are pending
                </span>
            </div>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            count: [],
            
        }
    },
    mounted() {
        this.taskStatusCounts();
    },
    computed: {
    completedPercent() {
        if (this.count.No_of_Tasks === 0) return 0; 
        return Math.round((this.count.No_of_completed_tasks / this.count.No_of_Tasks) * 100);
        },
    inProcessPercent() {
        if (this.count.No_of_Tasks === 0) return 0; 
        return Math.round((this.count.No_of_in_process_tasks / this.count.No_of_Tasks) * 100);
    },
    pendingPercent(){
        if (this.count.No_of_Tasks === 0) return 0; 
        return Math.round((this.count.No_of_pending_tasks / this.count.No_of_Tasks) * 100);
    }
     },
    methods: {
        // call count of status API 
        async taskStatusCounts(){
            console.log("taskStatusCounts Method is triggered")
            await axios
            .get('statusCount/')
            .then(response => {
                console.log("the response data is: ",response.data);
                this.count = response.data;
                // this.completed_percent = (this.count.No_of_completed_tasks/this.count.No_of_Tasks)*100 ;


            })
            .catch(error => {
                console.log("Error fetching count of task status: ", error)
            })
        }
        
    },
}
</script>

<style>

</style>




