import { createWebHistory, createRouter } from 'vue-router'
import HomePage from "@/views/HomePage.vue"
import PingTest from '../components/Ping.vue'
import PageNotFound from "@/views/PageNotFound.vue"

const routes = [{
        path: '/',
        name: 'HomePage',
        component: HomePage,
    }, {
        path: '/ping',
        name: 'PingTest',
        component: PingTest,
    },
    {
        path: '/:catchAll(.*)*',
        name: "PageNotFound",
        component: PageNotFound,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router