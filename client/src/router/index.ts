import { createRouter, createWebHistory } from 'vue-router'
import AboutView from '../views/AboutView.vue'
import EventsView from '../views/EventsView.vue'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'about',
      component: AboutView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/events',
      name: 'events',
      component: EventsView
    }
  ]
})

export default router
