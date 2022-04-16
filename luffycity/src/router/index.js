import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LightCourse from '../views/LightCourse.vue'
import ActualCourse from '../views/ActualCourse.vue'
import FreeCourse from '../views/FreeCourse.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/free-course',
    name: 'free-course',
    component: FreeCourse
  },
  {
    path: '/light-course',
    name: 'light-course',
    component: LightCourse
  },
  {
    path: '/actual-course',
    name: 'actual-course',
    component: ActualCourse
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
