import { createWebHistory, createRouter } from 'vue-router'
import PingTest from '../components/Ping.vue'

const routes = [{
    path: '/ping',
    name: 'PingTest',
    component: PingTest,
}]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router